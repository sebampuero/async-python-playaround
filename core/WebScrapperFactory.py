from .AmazonScrapper import AmazonScrapper
from .WebScrapper import WebScrapper

class WebScrapperFactory:

    @classmethod
    def get_web_scrapper(cls, url: str) -> WebScrapper:
        # via regex evaluate and return a scrapper
        return AmazonScrapper(url)