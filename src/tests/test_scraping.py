import unittest
from src.scraping.scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_scrape(self):
        scraper = Scraper("AAPL")
        data = scraper.scrape()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)
        self.assertIn("currentPrice", data)
        self.assertIsInstance(data["currentPrice"], float)

if __name__ == "__main__":
    unittest.main()

