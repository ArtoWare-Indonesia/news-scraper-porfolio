from utils.logger import setup_logger
from scrapers.antara import AntaraScraper

setup_logger()

scraper = AntaraScraper()

articles = scraper.scrape()

print(f"\nJumlah artikel: {len(articles)}")

for article in articles[:5]:
    print(article)
