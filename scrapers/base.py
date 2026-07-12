from abc import ABC, abstractmethod
import logging
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class BaseScraper(ABC):
    """Base class untuk semua HTML scraper."""

    def __init__(self, start_url):
        self.start_url = start_url
        self.logger = logging.getLogger(self.__class__.__name__)
        self.session = self._create_session()

    def _create_session(self):
        """Membuat requests.Session dengan retry otomatis."""

        session = requests.Session()

        retry = Retry(
            total=3,
            connect=3,
            read=3,
            backoff_factor=1,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504,
            ],
            allowed_methods=["GET"],
        )

        adapter = HTTPAdapter(max_retries=retry)

        session.mount("http://", adapter)
        session.mount("https://", adapter)

        session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/137.0 Safari/537.36"
            )
        })

        return session

    def fetch(self, url=None):
        """Mengambil halaman HTML."""

        target = url or self.start_url

        self.logger.info(f"Fetching: {target}")

        response = self.session.get(
            target,
            timeout=15,
        )

        response.raise_for_status()

        return response.text

    def get_soup(self, url=None):
        """Mengembalikan objek BeautifulSoup."""

        html = self.fetch(url)
        return BeautifulSoup(html, "html.parser")

    def is_valid_url(self, url):
        """
        Memvalidasi URL artikel.

        Mengembalikan True jika URL valid,
        False jika kosong atau bukan URL HTTP/HTTPS.
        """

        if not url:
            return False

        url = url.strip()

        if not url:
            return False

        if url.startswith("#"):
            return False

        if url.startswith("javascript:"):
            return False

        parsed = urlparse(url)

        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
        )

    def remove_duplicates(self, articles):
        """
        Menghapus artikel duplikat berdasarkan URL.
        """

        unique_articles = []
        seen_urls = set()

        for article in articles:
            url = article.get("url", "").strip()

            if not url:
                continue

            if url in seen_urls:
                continue

            seen_urls.add(url)
            unique_articles.append(article)

        removed = len(articles) - len(unique_articles)

        if removed > 0:
            self.logger.info(
                f"Removed {removed} duplicate articles"
            )

        return unique_articles

    def clean_text(self, text):
        """
        Membersihkan teks hasil scraping.
        """

        if text is None:
            return ""

        text = str(text)

        text = (
            text.replace("\n", " ")
                .replace("\r", " ")
                .replace("\t", " ")
        )

        text = " ".join(text.split())

        return text.strip()

    def clean_article(self, article):
        """
        Membersihkan seluruh field artikel.
        """

        cleaned = {}

        for key, value in article.items():
            cleaned[key] = self.clean_text(value)

        return cleaned

    def clean_articles(self, articles):
        """
        Membersihkan semua artikel.
        """

        cleaned_articles = [
            self.clean_article(article)
            for article in articles
        ]

        self.logger.info(
            f"Cleaned {len(cleaned_articles)} articles"
        )

        return cleaned_articles

    def scrape(self):
        """Workflow standar semua scraper."""

        self.logger.info(f"Running {self.__class__.__name__}")

        soup = self.get_soup()

        articles = self.parse(soup)

        articles = self.remove_duplicates(articles)

        articles = self.clean_articles(articles)

        self.logger.info(f"Collected {len(articles)} articles")

        return articles

    @abstractmethod
    def parse(self, soup):
        """Harus diimplementasikan oleh setiap scraper."""
        pass