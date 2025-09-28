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