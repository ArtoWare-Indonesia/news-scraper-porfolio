import time

from config import APP_NAME, APP_VERSION
from scrapers.manager import ScraperManager
from utils.exporter import Exporter
from utils.logger import setup_logger

logger = setup_logger()


def main(selected=None):
    """
    Menjalankan proses scraping.

    Parameters
    ----------
    selected : list[str] | None
        Daftar scraper yang akan dijalankan.
        Jika None, semua scraper dijalankan.
    """
    start_time = time.perf_counter()
    
    logger.info("=" * 50)
    logger.info("%s v%s", APP_NAME, APP_VERSION)
    logger.info("=" * 50)

    logger.info("Starting news scraping...")

    manager = ScraperManager()

    all_articles, source_counts, failed_sources = manager.run(
        selected=selected
    )

    if not all_articles:
        logger.warning("No articles collected.")
        return

    exporter = Exporter()
    exporter.export_all(all_articles)

    elapsed = time.perf_counter() - start_time

    logger.info("")
    logger.info("=" * 50)
    logger.info("SCRAPING SUMMARY")
    logger.info("=" * 50)

    logger.info("Sources")

    for source, count in source_counts.items():
        logger.info(
            "  • %-10s : %d article(s)",
            source,
            count
        )

    logger.info("-" * 50)

    if failed_sources:
        logger.warning(
            "Failed scraper(s): %s",
            ", ".join(failed_sources)
        )
    else:
        logger.info("Failed scraper(s): None")

    logger.info(
        "Total articles : %d",
        len(all_articles)
    )
    logger.info(
        "Export formats : CSV, JSON, Excel"
    )
    logger.info(
        "Output folder  : output/"
    )
    logger.info(
        "Elapsed time   : %.2f seconds",
        elapsed
    )
    logger.info("=" * 50)
    logger.info(
        "Scraping completed successfully!"
    )


if __name__ == "__main__":
    main()