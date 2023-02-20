from bson import ObjectId
from sanic import Sanic
import logging

logger = logging.getLogger(__name__)

class DAO:

    def __init__(self) -> None:
        app = Sanic.get_app()
        self.mongo_db = app.ctx.db
        self.collection = self.mongo_db.alarm_collection

    async def save(self, alarm: dict) -> str:
        result = await self.collection.insert_one(alarm)
        return str(result.inserted_id)

    async def delete(self, id: str) -> str:
        delete_result = await self.collection.delete_one({'_id': ObjectId(id)})
        return id if delete_result.deleted_count == 1 else ""

    async def get_alarms(self) -> list:
        alarms = []
        async for document in self.collection.find():
            alarms.append(document)
        return alarms