class FrontierManager:
    """
    Keeps a queue of URLs to visit and a set of visited URLs.
    """
    def __init__(self):
        self.to_visit = []
        self.visited = set()

    def add_url(self, url):
        """Add a new URL to the frontier if it hasn’t been seen yet."""
        if url and url not in self.visited and url not in self.to_visit:
            self.to_visit.append(url)

    def get_next_url(self):
        """Pop the next URL from the frontier."""
        if not self.to_visit:
            return None
        url = self.to_visit.pop(0)
        self.visited.add(url)
        return url
