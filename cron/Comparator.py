from persistance.DAO import DAO
from core.EmailNotifier import EmailNotifier

class Comparator:
    
    def __init__(self) -> None:
        self.dao = DAO()

    async def scan_links(self):
        all_alarms = await self.dao.get_alarms()
        # for every item, extract its link
        # then call a scrapper
        # gather price
        # compare prices and if there are news
        # call email notifier and inform about change!
        # afterwards delete the entry