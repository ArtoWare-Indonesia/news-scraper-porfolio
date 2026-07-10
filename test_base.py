from scrapers.base import BaseScraper


class TestScraper(BaseScraper):
    def scrape(self):
        soup = self.get_soup()
        print(soup.title.text)


scraper = TestScraper("https://example.com")
scraper.scrape()
