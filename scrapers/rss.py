import feedparser

from models import NewsItem
from .base import BaseScraper


class RSSScraper(BaseScraper):
    """Generic scraper untuk RSS Feed."""

    def __init__(self, source):
        super().__init__(source)

    def scrape(self):
        self.logger.info(
            "Running RSSScraper (%s)",
            self.source["name"]
        )

        articles = []

        feed = feedparser.parse(self.start_url)

        self.logger.info(
            "Found %d feed entries",
            len(feed.entries)
        )

        for entry in feed.entries:

            item = NewsItem(
                title=self.clean_text(
                    entry.get("title", "")
                ),
                url=entry.get("link", ""),
                source=self.source["name"],
                published=self.clean_text(
                    entry.get("published", "")
                ),
                summary=self.clean_text(
                    entry.get("summary", "")
                ),
            )

            articles.append(item.to_dict())

        articles = self.remove_duplicates(articles)

        self.logger.info(
            "Collected %d articles",
            len(articles)
        )

        return articles