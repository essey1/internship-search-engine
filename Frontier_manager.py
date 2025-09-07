# --------------------------
# Frontier Manager
# --------------------------
class FrontierManager:
    """
    Manages the crawling frontier: URLs to visit and visited URLs.
    """
    
    def __init__(self):
        self.to_visit = []       # URLs waiting to be crawled (the frontier)
        self.visited = set()     # URLs already crawled
    
    def add_url(self, url):
        """Add URL to the frontier if not visited and not already in queue."""
        url = url.strip()
        if url and url not in self.visited and url not in self.to_visit:
            self.to_visit.append(url)
    
    def get_next_url(self):
        """Return next URL from frontier and mark as visited."""
        if not self.to_visit:
            return None
        url = self.to_visit.pop(0)
        self.visited.add(url)
        return url

# --------------------------
# Demo showing the frontier
# --------------------------
if __name__ == "__main__":
    frontier = FrontierManager()

    # Add URLs to the frontier
    frontier.add_url("https://example.com/page1")
    frontier.add_url("https://example.com/page2")
    frontier.add_url("https://example.com/page3")

    # Check the frontier BEFORE crawling
    print("Frontier before crawling:", frontier.to_visit)
    # Output: ['https://example.com/page1', 'https://example.com/page2', 'https://example.com/page3']

    # Crawl URLs one by one
    while True:
        url = frontier.get_next_url()
        if not url:
            break
        print("Crawling:", url)
        print("Frontier now:", frontier.to_visit)
        print("Visited:", frontier.visited)

    # Final state
    print("Frontier after crawling:", frontier.to_visit)  # Should be empty
    print("All visited URLs:", frontier.visited)
