import asyncio
import logging

logger = logging.getLogger(__name__)

# NOTE: can be expanded in the future
async def simple_cron():
    while True:
        await asyncio.sleep(1800)