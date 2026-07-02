import feedparser
from scrapers.base import BaseScraper


class RSSScraper(BaseScraper):
    def scrape(self, source_name, rss_url):
        feed = feedparser.parse(rss_url)

        articles = []

        for entry in feed.entries:
            articles.append({
                "source": source_name,
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", "")
            })

        return articles