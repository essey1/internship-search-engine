import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://github.com/SimplifyJobs/Summer2026-Internships"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

session = requests.Session()
response = session.get(url, headers=headers)
time.sleep(2)  # polite delay

soup = BeautifulSoup(response.text, "html.parser")

# GitHub renders the README inside an <article> with class "markdown-body"
readme = soup.find("article", class_="markdown-body")

# find all tables in README
tables = readme.find_all("table")

jobs = []
for table in tables:
    headers = [th.get_text(strip=True) for th in table.find("tr").find_all("th")]
    for row in table.find_all("tr")[1:]:
        cells = [td.get_text(" ", strip=True) for td in row.find_all("td")]
        if cells:
            jobs.append(dict(zip(headers, cells)))

df = pd.DataFrame(jobs)
print(df.head())

df.to_csv("research_internships.csv", index=False)
