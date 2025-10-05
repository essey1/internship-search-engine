# test_seed.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# ---------- FrontierManager ----------
class FrontierManager:
    def __init__(self):
        self.to_visit = []
        self.visited = set()

    def add_url(self, url):
        if url not in self.visited and url not in self.to_visit:
            self.to_visit.append(url)

    def get_all_urls(self):
        return list(self.to_visit)

    def has_next(self):
        return len(self.to_visit) > 0

    def get_next_url(self):
        if self.to_visit:
            url = self.to_visit.pop(0)
            self.visited.add(url)
            return url
        return None

class AutoSeedCollector:
    def __init__(self, frontier_manager):
        self.frontier_manager = frontier_manager

    def discover_companies(self, hub_urls):
        if isinstance(hub_urls, str):
            hub_urls = [hub_urls]

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        }

        for hub in hub_urls:
            print(f"\nFetching hub page: {hub}")
            try:
                r = requests.get(hub, headers=headers, timeout=10)
                print("Status:", r.status_code)
                html = r.text
            except Exception as e:
                print(f"Error fetching {hub}: {e}")
                continue

            soup = BeautifulSoup(html, 'html.parser')
            found = 0
            for link in soup.find_all('a', href=True):
                full_url = urljoin(hub, link['href'])
                parsed = urlparse(full_url)
                if parsed.scheme in ('http', 'https'):
                    # For testing, don’t filter anything out
                    self.frontier_manager.add_url(full_url)
                    found += 1
            print(f"Added {found} links from {hub}")

# ---------- run test ----------
if __name__ == "__main__":
    frontier = FrontierManager()
    collector = AutoSeedCollector(frontier)

    # Pick a hub page that definitely has links
    hub_page = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"  # can also try "https://www.bbc.com"
    collector.discover_companies(hub_page)

    urls = frontier.get_all_urls()
    print("\n=== Results ===")
    print(f"Total URLs collected: {len(urls)}")
    for u in urls[:10]:  # show first 10
        print(u)
