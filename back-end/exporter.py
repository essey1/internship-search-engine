import csv

def save_opportunities_to_csv(opportunities, filename="opportunities.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Eligibility", "Link", "Type"])
        for opp in opportunities:
            writer.writerow([
                opp.title,
                opp.company,
                opp.location,
                opp.eligibility,
                opp.link,
                opp.type
            ])
    print(f"Saved {len(opportunities)} opportunities to {filename}")
