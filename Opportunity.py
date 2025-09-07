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
