from scrapers.manager import ScraperManager
from utils.exporter import Exporter
from utils.logger import setup_logger

logger = setup_logger()


def main():
    logger.info("Starting news scraping...")

    manager = ScraperManager()

    all_articles = manager.run()

    exporter = Exporter()

    exporter.export_all(all_articles)

    logger.info("")
    logger.info("Scraping completed successfully!")
    logger.info(f"Total articles: {len(all_articles)}")
    logger.info("Files saved in output/ folder")


if __name__ == "__main__":
    main()
