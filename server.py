# Hello world
import motor.motor_asyncio, sys, logging, socket
from logging.handlers import RotatingFileHandler
from asyncio import BoundedSemaphore
from sanic import Sanic
from controller.routes_controller import *
from cron.cronjob import simple_cron
from exceptions.DBNotRunningException import DBNotRunningException

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

async def start_sync_task():
    """
    If this process is to run the sync, start it https://github.com/sanic-org/sanic/issues/2139
    """

    max_runs = BoundedSemaphore()
    max_runs.acquire()
    await simple_cron()

def check_mongo_is_running() -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not sock.connect_ex(("localhost", 27017)) == 0:
        raise DBNotRunningException("MongoDB is not running")

# Initialize connection with DB, if not possible, stop app and throw error in logs
try:
    check_mongo_is_running()
    client = motor.motor_asyncio.AsyncIOMotorClient()
    app.ctx.db_client = client
except DBNotRunningException:
    logger.error("DB is not running, exiting...", exc_info=True)
    sys.exit()

app.add_task(start_sync_task)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)