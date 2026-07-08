from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """
    Base class untuk semua scraper.
    """

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def scrape(self):
        """
        Mengembalikan list of dictionary.
        """
        pass
