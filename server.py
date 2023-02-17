# Hello world
from sanic import Sanic

app = Sanic("price_alarm_app")

# Initialize cron here
# Initialize connection with DB, if not possible, stop app and throw error in logs

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)