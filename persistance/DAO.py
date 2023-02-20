from sanic import Sanic
from .AlarmEntity import AlarmEntity
import logging

logger = logging.getLogger(__name__)

class DAO:

    def __init__(self) -> None:
        app = Sanic.get_app()
        self.mongo_db = app.ctx.db
        self.collection = self.mongo_db.alarm_collection

    async def save(self, alarm: AlarmEntity) -> str:
        document = alarm.to_dict()
        result = await self.collection.insert_one(document)
        return str(result.inserted_id)

    async def delete(self, id: str) -> str:
        delete_result = await self.collection.delete_one({'_id': id})
        return id if delete_result.deleted_count == 1 else ""

    async def get_alarms(self) -> list:
        alarms = []
        async for document in self.collection.find():
            alarms.append(document)
        return alarms