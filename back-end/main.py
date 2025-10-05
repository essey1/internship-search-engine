from Frontier_manager import FrontierManager
from Seed_collector import AutoSeedCollector

if __name__ == "__main__":
    fm = FrontierManager()
    collector = AutoSeedCollector(fm)

    wiki_list = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
    collector.discover_career_pages(wiki_list)

    print("\nFrontier URLs:")
    while True:
        url = fm.get_next_url()
        if not url:
            break
        print("To crawl:", url)
