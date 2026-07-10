from utils.logger import setup_logger
from scrapers.manager import ScraperManager

setup_logger()

manager = ScraperManager()

articles = manager.run()

print()

print(f"TOTAL : {len(articles)} artikel")

print()

for article in articles[:10]:
    print(article)
