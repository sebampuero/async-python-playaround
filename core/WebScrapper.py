from abc import ABC, abstractmethod

class WebScrapper:

    def __init__(self, url: str) -> None:
        self.url = url

    @abstractmethod
    async def scrap_price_from_page(self):
        pass