from urllib.parse import urljoin

from models import NewsItem
from scrapers.base import BaseScraper


class TempoScraper(BaseScraper):
    """HTML scraper untuk Tempo."""

    BASE_URL = "https://www.tempo.co"

    def __init__(self, source):
        super().__init__(source)

    def parse(self, soup):
        articles = []

        cards = soup.select("figure.contents")

        self.logger.info(
            "Found %d article cards",
            len(cards)
        )

        for card in cards:

            link = card.select_one("figcaption a")

            if not link:
                continue

            title = link.get_text(strip=True)

            url = urljoin(
                self.BASE_URL,
                link.get("href", "")
            )

            if not self.is_valid_url(url):
                continue

            img = card.select_one("img")
            image = ""

            if img:
                image = (
                    img.get("src")
                    or img.get("data-src")
                    or ""
                )

            item = NewsItem(
                title=title,
                url=url,
                source=self.source["name"],
                image=image,
            )

            articles.append(item.to_dict())

        self.logger.info(
            "Parsed %d articles",
            len(articles)
        )

        return articles