import requests
from bs4 import BeautifulSoup
from opportunity import Opportunity

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MyCrawler/1.0; +https://example.com/bot)"
}


class BaseCrawler:
    """
    Takes URLs from FrontierManager, fetches HTML, passes to parser.
    """
    def __init__(self, frontier_manager, parser):
        self.frontier_manager = frontier_manager
        self.parser = parser

    def crawl(self):
        """
        Iterate through all URLs in frontier, parse them into Opportunity objects.
        """
        all_opps = []
        while True:
            url = self.frontier_manager.get_next_url()
            if not url:
                break

            print(f"Crawling: {url}")
            try:
                html = requests.get(url, headers=HEADERS, timeout=15).text
            except Exception as e:
                print(f"Error fetching {url}: {e}")
                continue

            soup = BeautifulSoup(html, 'html.parser')
            opps = self.parser.parse(soup, source_url=url)
            all_opps.extend(opps)

        return all_opps
