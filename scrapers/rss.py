import feedparser

from scrapers.base import BaseScraper


class RSSScraper(BaseScraper):
    """
    Scraper untuk RSS Feed.
    """

    def scrape(self):
        articles = []

        feed = feedparser.parse(self.source["url"])

        for entry in feed.entries:
            articles.append({
                "source": self.source["name"],
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", "")
            })

        return articles
