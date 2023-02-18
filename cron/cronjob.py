import asyncio

# NOTE: can be expanded in the future
async def simple_cron():
    while True:
        # do your logic here
        await asyncio.sleep(300)