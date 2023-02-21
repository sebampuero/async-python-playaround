import asyncio
import logging
from .Comparator import Comparator

logger = logging.getLogger(__name__)

# NOTE: can be expanded in the future
async def simple_cron():
    comp =  Comparator()
    while True:
        await asyncio.sleep(1800)
        await comp.scan_links()