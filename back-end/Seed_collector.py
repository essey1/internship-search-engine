import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MyCrawler/1.0; +https://example.com/bot)"
}


class AutoSeedCollector:
    def __init__(self, frontier_manager):
        self.frontier_manager = frontier_manager

    def _get_official_website(self, wiki_url):
        """
        Given a company's Wikipedia page, extract its official website
        from the infobox row labelled 'Website', falling back to first external link.
        """
        try:
            html = requests.get(wiki_url, headers=HEADERS, timeout=10).text
        except Exception as e:
            print(f"Error fetching {wiki_url}: {e}")
            return None

        soup = BeautifulSoup(html, 'html.parser')
        infobox = soup.find('table', class_='infobox')
        if not infobox:
            return None

        # 1. Look for row with header 'Website'
        for row in infobox.find_all('tr'):
            th = row.find('th')
            if th and 'Website' in th.get_text():
                a = row.find('a', href=True)
                if a and a['href'].startswith('http'):
                    return a['href']

        # 2. Look for any external text link in the infobox
        ext = infobox.find('a', class_='external text', href=True)
        if ext and ext['href'].startswith('http'):
            return ext['href']

        # 3. Fallback: first external http link in the infobox
        for a in infobox.find_all('a', href=True):
            href = a['href']
            if href.startswith('http'):
                return href

        return None


    # def _guess_career_page(self, official_url):
    #     """
    #     Given an official URL, try to guess its career page by appending
    #     common paths like /careers or /jobs.
    #     """
    #     if not official_url:
    #         return None

    #     base = official_url.rstrip('/')
    #     candidates = [
    #         base + '/careers',
    #         base + '/jobs',
    #         base + '/career',
    #         base + '/about/careers',
    #     ]
    #     for c in candidates:
    #         try:
    #             resp = requests.head(c, headers=HEADERS, timeout=5, allow_redirects=True)
    #             if resp.status_code < 400:
    #                 return resp.url  # follow redirect
    #         except Exception:
    #             continue
    #     return None

    def discover_career_pages(self, wikipedia_list_url):
        """
        Scrape the list page on Wikipedia, extract company names and wiki links,
        then resolve official site and career page, and push those URLs
        into the frontier manager.
        """
        html = requests.get(wikipedia_list_url, headers=HEADERS, timeout=10).text
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', class_='wikitable sortable')
        if not table:
            print("No company table found.")
            return

        rows = table.find_all('tr')[1:]  # skip header row
        for row in rows:
            cells = row.find_all('td')
            if not cells:
                continue
            company_link = cells[1].find('a', href=True)
            if not company_link:
                continue

            company_name = company_link.get_text(strip=True)
            wiki_url = urljoin(wikipedia_list_url, company_link['href'])

            official = self._get_official_website(wiki_url)
            career = self._discover_job_search_page(official)

            print(f"{company_name}: wiki={wiki_url}, official={official}, career={career}")

            if career:
                self.frontier_manager.add_url(career)
    

    def _discover_job_search_page(self, official_url):
        """
        Try to find the real job listings/search page by:
        1. Guessing common career URLs
        2. Opening the career page and scanning for job search links
        """
        if not official_url:
            return None

        base = official_url.rstrip('/')
        candidates = [
            base + '/careers',
            base + '/jobs',
            base + '/career',
            base + '/about/careers',
        ]

        for c in candidates:
            try:
                resp = requests.get(c, headers=HEADERS, timeout=10)
                if resp.status_code >= 400:
                    continue

                soup = BeautifulSoup(resp.text, 'html.parser')

                # Look for links containing job-related text
                for a in soup.find_all('a', href=True):
                    text = a.get_text(strip=True).lower()
                    if any(keyword in text for keyword in ['search', 'jobs', 'careers', 'openings', 'apply']):
                        href = a['href']
                        full_url = urljoin(c, href)
                        if full_url.startswith('http'):
                            return full_url  # Found real job search engine link

                # If no internal link found, still return valid career page
                return c

            except Exception:
                continue

        return None

