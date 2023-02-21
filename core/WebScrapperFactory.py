from .AmazonScrapper import AmazonScrapper
from .WebScrapper import WebScrapper
import re

class WebScrapperFactory:

    @classmethod
    def get_web_scrapper(cls, url: str) -> WebScrapper:
        if len(re.findall("(amazon\.)(de|com)", url)) > 0:
            return AmazonScrapper()