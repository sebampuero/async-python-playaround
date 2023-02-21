from .WebScrapper import WebScrapper
from bs4 import BeautifulSoup

class AmazonScrapper(WebScrapper):
    
    async def scrap_price_from_page(self, html: str):
        pass