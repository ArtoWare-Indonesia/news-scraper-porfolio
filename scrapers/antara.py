from urllib.parse import urljoin

from models import NewsItem
from .base import BaseScraper


class AntaraScraper(BaseScraper):

    BASE_URL = "https://www.antaranews.com"
    START_URL = "https://www.antaranews.com/terkini"

    def __init__(self):
        super().__init__(self.START_URL)

    def parse(self, soup):
        articles = []

        cards = soup.select("div.card__post__body")

        self.logger.info(f"Found {len(cards)} article cards")

        for card in cards:

            title_tag = card.select_one("h2.post_title a")

            if title_tag is None:
                continue

            title = title_tag.get_text(strip=True)

            url = urljoin(
                self.BASE_URL,
                title_tag.get("href", "")
            )

            category_tag = card.select_one("h4.slug a")
            category = (
                category_tag.get_text(strip=True)
                if category_tag
                else ""
            )

            time_tag = card.select_one(
                "div.card__post__author-info span"
            )
            published = (
                time_tag.get_text(strip=True)
                if time_tag
                else ""
            )

            summary_tag = card.select_one("p")
            summary = (
                summary_tag.get_text(strip=True)
                if summary_tag
                else ""
            )

            item = NewsItem(
                title=title,
                url=url,
                source="Antara",
                category=category,
                published=published,
                summary=summary,
            )

            if not self.is_valid_url(url):
                continue
            
            articles.append(item.to_dict())

        self.logger.info(f"Parsed {len(articles)} articles")

        return articles
