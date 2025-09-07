import requests
from bs4 import BeautifulSoup

class Crawler:
    """
    Base class for fetching web pages and storing their HTML content.
    
    Attributes:
        url (str): URL of the page to crawl.
        soup (BeautifulSoup object): Parsed HTML of the fetched page.
    """
    def __init__(self, url):
        self.url = url
        self.soup = None
    
    # Fetch the page HTML
    def fetch_page(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()  # raise exception for HTTP errors
            self.soup = BeautifulSoup(response.text, "html.parser")
            return self.soup
        except requests.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            return None
    
    # extract links from the page for further crawling
    def extract_links(self):
        if not self.soup:
            print("Page not fetched yet. Run fetch_page() first.")
            return []
        
        links = []
        for a_tag in self.soup.find_all("a", href=True):
            links.append(a_tag["href"])
        
        return links
