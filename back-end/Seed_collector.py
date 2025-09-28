import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class AutoSeedCollector:
    def __init__(self, frontier_manager):
        self.frontier_manager = frontier_manager

    def discover_companies(self, hub_urls):
        """
        Take one or more 'hub' URLs (like a directory or a Wikipedia page)
        and automatically add outbound company URLs as seeds.
        """
        if isinstance(hub_urls, str):
            hub_urls = [hub_urls]

        for hub in hub_urls:
            try:
                html = requests.get(hub, timeout=10).text
            except Exception as e:
                print(f"Error fetching {hub}: {e}")
                continue

            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a', href=True):
                full_url = urljoin(hub, link['href'])
                parsed = urlparse(full_url)
                if parsed.scheme in ('http', 'https'):
                    # naive filter: skip Wikipedia/LinkedIn etc.
                    if 'wikipedia.org' not in parsed.netloc:
                        self.frontier_manager.add_url(full_url)
