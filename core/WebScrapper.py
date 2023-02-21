from abc import ABC, abstractmethod

class WebScrapper(ABC):

    @abstractmethod
    async def scrap_price_from_page(self, html: str):
        pass