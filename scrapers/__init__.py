# Package initialization
from .antara import AntaraScraper
from .tempo import TempoScraper

SCRAPERS = [
    AntaraScraper,
    TempoScraper,
]
