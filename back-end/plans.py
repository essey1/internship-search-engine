# --------------------------
# Data Model
# --------------------------
class Opportunity:
    """
    Represents a single opportunity (internship, research, or career program).
    
    Attributes:
        title (str): Title of the opportunity.
        company (str): Name of the organization/company offering the opportunity.
        location (str): Location of the opportunity (city, country, or remote).
        eligibility (str): Eligibility for F-1/CPT/OPT international students.
        link (str): URL link to the opportunity posting.
        type (str): Type of opportunity ("Internship", "Research", "Program").
    """
    def __init__(self, title=None, company=None, location=None, eligibility=None, link=None, type_=None):
        self.title = title
        self.company = company
        self.location = location
        self.eligibility = eligibility
        self.link = link
        self.type = type_
    
    # Placeholder for cleaning or validating data
    def clean_data(self):
        pass

    # Optional: check if opportunity is suitable for international students
    def is_international_friendly(self):
        pass

# --------------------------
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

# --------------------------
# Frontier Manager
# --------------------------
class FrontierManager:
    """
    Manages the list of URLs to visit and keeps track of visited URLs.
    
    Attributes:
        to_visit (list): Queue of URLs that need to be crawled.
        visited (set): Set of URLs that have already been crawled.
    
    Purpose:
        - Avoid crawling the same page multiple times.
        - Provide a centralized place to manage the crawling frontier.
    """
    def __init__(self):
        self.to_visit = []       # Queue of URLs to visit
        self.visited = set()     # Set of visited URLs
    
    def add_url(self, url):
        pass
    
    def get_next_url(self):
        pass

# --------------------------
# Base Parser
# --------------------------
class Parser:
    """
    Base class for parsing HTML content and extracting opportunity data.
    
    Purpose:
        - Encapsulates site-specific parsing logic.
        - Returns a list of Opportunity objects extracted from a page.
    """
    def parse(self, soup):
        pass

# Example of a site-specific parser
class SiteParser(Parser):
    """
    Example parser for a specific website structure.
    
    Purpose:
        - Overrides the parse method to extract opportunities from known HTML layout.
    """
    def parse(self, soup):
        pass

# --------------------------
# Crawler Manager
# --------------------------
class CrawlerManager:
    """
    Orchestrates the crawling process, manages the frontier, and aggregates data.
    
    Attributes:
        frontier (FrontierManager): Manages URLs to visit and visited URLs.
        opportunities (list): List of Opportunity objects collected from crawled pages.
    
    Purpose:
        - Coordinates crawling and parsing.
        - Keeps track of all collected opportunities.
        - Provides methods to save collected data.
    """
    def __init__(self):
        self.frontier = FrontierManager()
        self.opportunities = []  # List of Opportunity objects
    
    # Add seed URLs to start crawling
    def add_seed(self, url):
        pass
    
    # Main crawling loop
    def crawl(self, parser_class, max_pages=100):
        pass
    
    # Save collected opportunities to CSV, database, etc.
    def save_data(self, filename="opportunities.csv"):
        pass
