# --------------------------
# Frontier Manager
# --------------------------
class FrontierManager:
    """
    Manages the list of URLs to visit (frontier) and keeps track of visited URLs.
    
    Attributes:
        to_visit (list): Queue of URLs that still need to be crawled.
        visited (set): Set of URLs that have already been crawled.
    
    Purpose:
        - Avoid visiting the same URL multiple times.
        - Provide a central place to manage which URLs to crawl next.
    """
    
    def __init__(self):
        """
        Initializes an empty frontier.
        """
        self.to_visit = []       # Queue of URLs to visit (FIFO)
        self.visited = set()     # Set of URLs that have already been visited
    
    def add_url(self, url):
        """
        Adds a new URL to the frontier.
        
        Args:
            url (str): The URL to add.
            
        Notes:
            - Strips extra spaces.
            - Will NOT add the URL if it has already been visited.
            - Will NOT add the URL if it is already in the queue.
        """
        url = url.strip()  # remove leading/trailing whitespace
        if url not in self.visited and url not in self.to_visit:
            self.to_visit.append(url)  # add to the end of the queue
    
    def get_next_url(self):
        """
        Returns the next URL to crawl from the frontier.
        
        Returns:
            str or None: The next URL to visit, or None if the frontier is empty.
        
        Notes:
            - Removes the URL from the queue (FIFO order).
            - Marks the URL as visited by adding it to the visited set.
        """
        if not self.to_visit:
            return None  # no URLs left to visit
        url = self.to_visit.pop(0)  # take the first URL from the queue
        self.visited.add(url)       # mark it as visited
        return url
