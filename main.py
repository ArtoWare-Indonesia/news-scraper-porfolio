from config import RSS_SOURCES
from scrapers.rss_scraper import RSSScraper
from utils.exporter import Exporter
from utils.logger import setup_logger


def main():
    scraper = RSSScraper()
    exporter = Exporter()
    logger = setup_logger() 


    all_articles = []

    logger.info("Starting news scraping...")

    for source_name, rss_url in RSS_SOURCES.items():
        try:
            logger.info(f"Scraping {source_name}...")

            articles = scraper.scrape(source_name, rss_url)

            logger.info(f"Found {len(articles)} articles")

            all_articles.extend(articles)

        except Exception as e:
            logger.error(f"Error scraping {source_name}: {e}")

    if all_articles:
        exporter.to_csv(all_articles)
        exporter.to_excel(all_articles)
        exporter.to_json(all_articles)

        logger.info("\nScraping completed successfully!")
        logger.info(f"Total articles: {len(all_articles)}")
        logger.info("Files saved in output/ folder")

    else:
        logger.error("\nNo articles found.")


if __name__ == "__main__":
    main()
