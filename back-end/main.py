from Frontier_manager import FrontierManager
from Seed_collector import AutoSeedCollector
from base_crawler import BaseCrawler
from parser import GenericCareerParser
from exporter import save_opportunities_to_csv

if __name__ == "__main__":
    fm = FrontierManager()
    collector = AutoSeedCollector(fm)

    wiki_list = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
    collector.discover_career_pages(wiki_list)

    parser = GenericCareerParser()
    crawler = BaseCrawler(fm, parser)

    opportunities = crawler.crawl()

    save_opportunities_to_csv(opportunities)
