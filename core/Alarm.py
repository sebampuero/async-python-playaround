from EmailNotifier import EmailNotifier
from persistance.AlarmEntity import AlarmEntity

class Alarm:

    def __init__(self) -> None:
        self.email_notifier = EmailNotifier()

    async def create_alarm(alarm: AlarmEntity) -> str:
        # call DAO and create alarm, return the ID
        # call email notifier if successful and send email with link + id (we can use app generate url for this)
        # return the id
        return ""

    async def delete_alarm(id: str) -> str:
        # call DAO and delete alarm with given ID
        # return id if successful
        return ""

    async def get_alarms() -> dict:
        # call DAO and retrieve all alarms
        # put them in a dict and return 
        return {}