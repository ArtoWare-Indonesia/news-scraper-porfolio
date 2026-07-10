from utils.logger import setup_logger
from scrapers.tempo import TempoScraper

setup_logger()

scraper = TempoScraper()

articles = scraper.scrape()

print(f"\nJumlah artikel: {len(articles)}")

for article in articles[:5]:
    print(article)
