from sanic import Sanic
from AlarmEntity import AlarmEntity

class DAO:

    def __init__(self) -> None:
        app = Sanic.get_app()
        self.mongo_client = app.ctx.db_client

    async def save(alarm: AlarmEntity) -> str:
        pass

    async def delete(id: str) -> str:
        pass

    async def get_alarms() -> dict:
        pass