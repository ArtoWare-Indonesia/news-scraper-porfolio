from scrapers import SCRAPERS


class ScraperManager:
    """Menjalankan semua scraper yang terdaftar."""

    def __init__(self):
        self.scrapers = [
            scraper_class()
            for scraper_class in SCRAPERS
        ]

    def run(self):
        all_articles = []

        for scraper in self.scrapers:

            scraper.logger.info(
                f"Running {scraper.__class__.__name__}"
            )

            try:
                articles = scraper.scrape()

                scraper.logger.info(
                    f"Collected {len(articles)} articles"
                )

                all_articles.extend(articles)

            except Exception:

                scraper.logger.exception(
                    f"Failed running {scraper.__class__.__name__}"
                )

        return all_articles
