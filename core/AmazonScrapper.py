from .WebScrapper import WebScrapper


class AmazonScrapper(WebScrapper):
    
    async def scrap_price_from_page(self):
        # use an async scrapper to return the price from page
        return await super().scrap_price_from_page()