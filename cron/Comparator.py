from persistance.DAO import DAO
from core.EmailNotifier import EmailNotifier
from core.WebScrapperFactory import WebScrapperFactory
import aiohttp, asyncio, logging

logger = logging.getLogger(__name__)

class Comparator:
    
    def __init__(self) -> None:
        self.dao = DAO()

    async def scan_links(self):
        all_alarms = await self.dao.get_alarms()
        logger.debug(f"Checking pages from: {all_alarms}")
        async with aiohttp.ClientSession() as session:
            for alarm in all_alarms:
                url = alarm['url']
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
                async with session.get(url, headers=headers) as response:
                    logger.debug(f"Established connection with {url} on session {session}")
                    webscrapper = WebScrapperFactory.get_web_scrapper(url)
                    if not webscrapper:
                        await EmailNotifier().send_email(f"{url} is still not supported.", alarm['email'])
                        await self.dao.delete(str(alarm['_id']))
                        continue
                    found_price = await webscrapper.scrap_price_from_page(await response.text())
                    logger.info(f"Found price {found_price} for {url}")
                    if not found_price:
                        logger.debug(f"No price found in {url}")
                        await EmailNotifier().send_email(f"{url} seems to be invalid :/, retry with other link or make sure the link contains a valid price to look for", alarm['email'])
                        await self.dao.delete(str(alarm['_id']))
                    if found_price >= alarm["price_from"] and found_price <= alarm["price_to"]:
                        await EmailNotifier().send_email(f"New price found for {url}!", alarm['email'])
                        await self.dao.delete(str(alarm['_id']))
                    await asyncio.sleep(3)