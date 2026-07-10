from urllib.parse import urljoin

from models import NewsItem
from .base import BaseScraper


class TempoScraper(BaseScraper):

    BASE_URL = "https://www.tempo.co"
    START_URL = "https://www.tempo.co"

    def __init__(self):
        super().__init__(self.START_URL)

    def parse(self, soup):
        articles = []

        cards = soup.select("figure.contents")

        self.logger.info(f"Found {len(cards)} article cards")

        for card in cards:

            link = card.select_one("figcaption a")

            if not link:
                continue

            title = link.get_text(strip=True)

            url = urljoin(
                self.BASE_URL,
                link.get("href", "")
            )

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
                source="Tempo",
                image=image,
            )

            articles.append(item.to_dict())

        self.logger.info(f"Parsed {len(articles)} articles")

        return articles
