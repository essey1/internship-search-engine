import requests
from bs4 import BeautifulSoup
import pandas as pd

# Search query: "research internship" in USA
url = "https://www.indeed.com/jobs?q=research+internship&l=United+States"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []
for job_card in soup.find_all("div", class_="job_seen_beacon"):
    title = job_card.find("h2").text.strip() if job_card.find("h2") else None
    company = job_card.find("span", class_="companyName").text.strip() if job_card.find("span", class_="companyName") else None
    location = job_card.find("div", class_="companyLocation").text.strip() if job_card.find("div", class_="companyLocation") else None
    summary = job_card.find("div", class_="job-snippet").text.strip() if job_card.find("div", class_="job-snippet") else None

    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Summary": summary
    })

df = pd.DataFrame(jobs)
print(df.head())
df.to_csv("research_internships.csv", index=False)
