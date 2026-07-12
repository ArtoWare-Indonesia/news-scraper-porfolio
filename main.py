import time

from scrapers.manager import ScraperManager
from utils.exporter import Exporter
from utils.logger import setup_logger

logger = setup_logger()


def main():
    start_time = time.perf_counter()

    logger.info("Starting news scraping...")

    manager = ScraperManager()

    all_articles = manager.run()

    exporter = Exporter()
    exporter.export_all(all_articles)

    elapsed = time.perf_counter() - start_time

    logger.info("")
    logger.info("=" * 50)
    logger.info("SCRAPING SUMMARY")
    logger.info("=" * 50)
    logger.info(f"Total articles : {len(all_articles)}")
    logger.info("Export formats : CSV, JSON, Excel")
    logger.info("Output folder  : output/")
    logger.info(f"Elapsed time   : {elapsed:.2f} seconds")
    logger.info("=" * 50)
    logger.info("Scraping completed successfully!")


if __name__ == "__main__":
    main()