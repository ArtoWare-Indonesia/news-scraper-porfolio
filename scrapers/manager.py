import logging

from config import HTML_SOURCES, RSS_SOURCES
from scrapers.registry import HTML_SCRAPERS
from scrapers.rss import RSSScraper


class ScraperManager:
    """Mengelola dan menjalankan scraper HTML dan RSS."""

    def __init__(self):
        self.html_scrapers = []
        self.rss_scrapers = []

        # HTML scraper
        for source in HTML_SOURCES:

            if not source.get("enabled", True):
                continue

            scraper_class = HTML_SCRAPERS.get(
                source["name"]
            )

            if scraper_class is None:
                continue

            self.html_scrapers.append(
                scraper_class(source)
            )

        # RSS scraper
        for source in RSS_SOURCES:

            if not source.get("enabled", True):
                continue

            self.rss_scrapers.append(
                RSSScraper(source)
            )

    def get_scrapers(self):
        """Mengembalikan seluruh scraper yang aktif."""
        return self.html_scrapers + self.rss_scrapers

    def run(self, selected=None):
        """
        Menjalankan scraper.

        Parameters
        ----------
        selected : list[str] | None
            Daftar nama source yang akan dijalankan.
            Jika None, semua scraper aktif dijalankan.

        Returns
        -------
        tuple[list, dict, list]
            (
                all_articles,
                {
                    "Antara": 15,
                    "Tempo": 45,
                    ...
                },
                [
                    "Tempo",
                    ...
                ]
            )
        """

        scrapers = self.get_scrapers()

        if selected:

            selected = {
                name.lower()
                for name in selected
            }

            scrapers = [
                scraper
                for scraper in scrapers
                if scraper.source["name"].lower()
                in selected
            ]

        if not scrapers:
            return [], {}, []

        logger = logging.getLogger("ScraperManager")

        logger.info(
            "Running %d scraper(s)...",
            len(scrapers)
        )

        all_articles = []
        source_counts = {}
        failed_sources = []

        for scraper in scrapers:

            source_name = scraper.source["name"]

            logger.info(
                "Running %s (%s)",
                scraper.__class__.__name__,
                source_name
            )

            try:

                articles = scraper.scrape()
                count = len(articles)

                source_counts[source_name] = count

                logger.info(
                    "%s collected %d article(s)",
                    source_name,
                    count
                )

                all_articles.extend(articles)

            except Exception:

                source_counts[source_name] = 0
                failed_sources.append(source_name)

                logger.exception(
                    "Failed running %s",
                    source_name
                )

        logger.info(
            "Finished. Total articles collected: %d",
            len(all_articles)
        )

        return (
            all_articles,
            source_counts,
            failed_sources,
        )