from opportunity import Opportunity

class GenericCareerParser:
    """
    Very naive parser: finds all links containing 'job' or 'career'
    and creates Opportunity objects.
    """
    def parse(self, soup, source_url=None):
        opps = []
        for a in soup.find_all('a', href=True):
            text = a.get_text(strip=True)
            href = a['href']
            if any(word in text.lower() for word in ["job", "career", "internship"]):
                opp = Opportunity(
                    title=text or "Career Opportunity",
                    company=self._guess_company_name(source_url),
                    location=None,
                    eligibility=None,
                    link=href if href.startswith("http") else source_url.rstrip("/") + "/" + href.lstrip("/"),
                    type_="Career Program"
                )
                opp.clean_data()
                opps.append(opp)
        return opps

    def _guess_company_name(self, url):
        """
        Derive company name from domain, e.g., 'https://www.coca-cola.com/careers' -> 'Coca-Cola'
        """
        if not url:
            return None
        host = url.split("//")[-1].split("/")[0]
        parts = host.replace("www.", "").split(".")[0]
        return parts.title()
