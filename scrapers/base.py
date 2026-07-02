import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from abc import ABC, abstractmethod
from config import HEADERS


class BaseScraper(ABC):

    def __init__(self):
        self.headers = HEADERS

        self.session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )

        adapter = HTTPAdapter(max_retries=retry)

        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def fetch(self, url):
        response = self.session.get(
            url,
            headers=self.headers,
            timeout=15
        )

        response.raise_for_status()

        return response

    @abstractmethod
    def scrape(self):
        pass