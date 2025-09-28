class Opportunity:
    """
    Represents a single opportunity (internship, research, or career program).
    
    Attributes:
        title (str): Title of the opportunity.
        company (str): Name of the organization/company offering the opportunity.
        location (str): Location of the opportunity (city, country, or remote).
        eligibility (str): Eligibility for F-1/CPT/OPT international students.
        link (str): URL link to the opportunity posting.
        type (str): Type of opportunity ("Internship", "Research", "Career Program").
    """
    def __init__(self, title=None, company=None, location=None, eligibility=None, link=None, type_=None):
        self.title = title
        self.company = company
        self.location = location
        self.eligibility = eligibility
        self.link = link
        self.type = type_
    
    # Method to clean or validate data
    def clean_data(self):
        # Strip whitespace and normalize case
        if self.title:
            self.title = self.title.strip().title()  # " software engineer " → "Software Engineer"
        if self.company:
            self.company = self.company.strip().title()
        if self.location:
            self.location = self.location.strip()

        # Standardize eligibility text
        if self.eligibility:
            self.eligibility = self.eligibility.strip().capitalize()

        # Validate link format
        if self.link and not self.link.startswith(("http://", "https://")):
            self.link = "https://" + self.link.strip()

        # Normalize type
        if self.type:
            self.type = self.type.strip().capitalize()

    # check if opportunity is suitable for international students
    def is_international_friendly(self):
        if not self.eligibility:
            return None  # No info

        text = self.eligibility.lower()

        if "international" in text or "open to all" in text:
            return True
        if "us citizen" in text or "green card" in text:
            return False

        return None  # Unclear
