from abc import ABC, abstractmethod
import logging

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
        """Mengembalikan BeautifulSoup."""

        html = self.fetch(url)
        return BeautifulSoup(html, "html.parser")

    def scrape(self):
        """Workflow standar semua scraper."""

        soup = self.get_soup()
        return self.parse(soup)

    @abstractmethod
    def parse(self, soup):
        """Harus diimplementasikan oleh subclass."""
        pass
