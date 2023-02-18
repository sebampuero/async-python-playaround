# Hello world
import motor.motor_asyncio
import sys
import logging
from logging.handlers import RotatingFileHandler
from asyncio import BoundedSemaphore
from sanic import Sanic
from controller.routes_controller import *
from cron.cronjob import simple_cron

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler = RotatingFileHandler("/home/pi/price_alarm/alarm.log")
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

app = Sanic("price_alarm_app")
app.add_route(main_index, "/")
app.add_route(price_alarm_create, "/price-alarm", methods=["POST"])
app.add_route(price_alarm_delete, "/price-alarm/<id:uuid>", methods=["DELETE"])

# Initialize connection with DB, if not possible, stop app and throw error in logs
try:
    client = motor.motor_asyncio.AsyncIOMotorClient()
    app.ctx.db_client = client
except:
    logger.error("Could not connect to DB, exiting...", exc_info=True)
    sys.exit()

async def start_sync_task():
    """
    If this process is to run the sync, start it https://github.com/sanic-org/sanic/issues/2139
    """
    concurrency = 1

    max_runs = BoundedSemaphore(value=concurrency)

    with max_runs:
        await simple_cron()

if __name__ == "__main__":
    app.add_task(start_sync_task)
    app.run(host="0.0.0.0", port=8000)