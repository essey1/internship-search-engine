# Base Crawler
# --------------------------
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
        pass
    
    # Optional: extract links from the page for further crawling
    def extract_links(self):
        pass