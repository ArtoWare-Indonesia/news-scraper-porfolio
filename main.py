import time

from config import APP_NAME, APP_VERSION
from scrapers.manager import ScraperManager
from utils.cli import parse_args
from utils.exporter import Exporter
from utils.logger import setup_logger

logger = setup_logger()


def main():
    """
    Menjalankan proses scraping melalui Command Line Interface.
    """
    args = parse_args()

    selected = [args.source] if args.source else None

    logger.info("Source : %s", args.source)
    logger.info("Format : %s", args.format)
    logger.info("Limit  : %s", args.limit)

    start_time = time.perf_counter()

    logger.info("=" * 60)
    logger.info("%s v%s", APP_NAME, APP_VERSION)
    logger.info("=" * 60)
    logger.info("Starting news scraping...")

    manager = ScraperManager()

    all_articles, source_counts, failed_sources = manager.run(
        selected=selected
    )

    if args.limit is not None:
        logger.info(
            "Limiting export to %d article(s).",
            args.limit,
        )
        all_articles = all_articles[:args.limit]

    exported_files = []

    if all_articles:
        exporter = Exporter()
        exported_files = exporter.export_all(all_articles, export_format=args.format,)
    else:
        logger.warning("No articles collected.")

    elapsed = time.perf_counter() - start_time

    successful_sources = len(source_counts) - len(failed_sources)

    logger.info("")
    logger.info("=" * 60)
    logger.info("SCRAPING SUMMARY")
    logger.info("=" * 60)

    logger.info("Version           : %s", APP_VERSION)
    logger.info("Successful        : %d", successful_sources)
    logger.info("Failed            : %d", len(failed_sources))
    logger.info("Exported articles : %d", len(all_articles))

    logger.info("")
    logger.info("Articles by source")

    for source, count in source_counts.items():
        logger.info(
            "  %-15s : %d article(s)",
            source,
            count,
        )

    if failed_sources:
        logger.info("")
        logger.warning(
            "Failed source(s): %s",
            ", ".join(failed_sources),
        )

    logger.info("")
    logger.info("Exported files")

    if exported_files:
        for filepath in exported_files:
            logger.info("  - %s", filepath)
    else:
        logger.info("  None")

    logger.info("")
    logger.info(
        "Elapsed time      : %.2f seconds",
        elapsed,
    )

    logger.info("=" * 60)
    logger.info("Scraping completed successfully!")


if __name__ == "__main__":
    main()