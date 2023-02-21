from persistance.DAO import DAO
from core.EmailNotifier import EmailNotifier
from core.WebScrapperFactory import WebScrapperFactory
import aiohttp, asyncio

class Comparator:
    
    def __init__(self) -> None:
        self.dao = DAO()

    async def scan_links(self):
        all_alarms = await self.dao.get_alarms()
        for alarm in all_alarms:
            url = alarm.url
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    webscrapper = WebScrapperFactory.get_web_scrapper(await response.text())
                    found_price = webscrapper.scrap_price_from_page()
                    if not found_price:
                        EmailNotifier().send_email(f"{url} seems to be invalid :/, retry with other link or make sure the link contains a valid price to look for")
                    if found_price >= alarm.price_from and found_price <= alarm.price_to:
                        EmailNotifier().send_email(f"New price found for {url}!")
                    await self.dao.delete(str(alarm._id))
                    await asyncio.sleep(1)