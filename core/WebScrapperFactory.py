from .AmazonScrapper import AmazonScrapper
from .WebScrapper import WebScrapper
import re

class WebScrapperFactory:

    @classmethod
    def get_web_scrapper(cls, url: str) -> WebScrapper:
        if re.match(r"(amazon\.)(de|com)", url):
            return AmazonScrapper(url)