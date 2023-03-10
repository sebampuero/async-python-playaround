from .EmailNotifier import EmailNotifier
from persistance.AlarmEntity import AlarmEntity
from persistance.DAO import DAO
from sanic import Sanic
import logging

logger = logging.getLogger(__name__)

class Alarm:

    def __init__(self) -> None:
        self.email_notifier = EmailNotifier()
        self.dao = DAO()

    async def create_alarm(self, alarm: AlarmEntity):
        id = await self.dao.save(alarm.to_dict())
        logger.debug(f"Successfully created alarm with ID {id}")
        app = Sanic.get_app()
        msg = f"""
        Created! Here is your link in case you want to delete it and create again: {app.ctx.domain}{app.url_for('price_alarm_delete', id=id)}
        """
        await self.email_notifier.send_email(msg, alarm.email)
        return id

    async def delete_alarm(self, id: str):
        deleted_id = await self.dao.delete(id)
        logger.debug(f"Deleted entry with ID {deleted_id}")
        return deleted_id

    async def get_alarms(self):
        all_alarms = await self.dao.get_alarms()
        logger.debug(f"Gathering alarms: {all_alarms}")
        return all_alarms