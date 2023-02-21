from .WebScrapper import WebScrapper
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

class AmazonScrapper(WebScrapper):
    
    async def scrap_price_from_page(self, html: str) -> float:
        soup = BeautifulSoup(html, 'html.parser')
        try:
            price_whole = soup.find('span', class_='a-price-whole').text.replace(',', '.')
            price_fraction = soup.find('span', class_='a-price-fraction').text
            return float(price_whole + price_fraction)
        except Exception:
            logger.error("Scrapped link has no value, it will be deleted", exc_info=True)
            return None