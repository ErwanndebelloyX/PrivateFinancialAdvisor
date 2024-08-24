import unittest
from src.scraping.scraper import Scraper
from src.scraping.newspaper import Newspaper
symbols = ['AAPL', 'GOOGL', 'AMZN', 'TSLA']

class TestScraper(unittest.TestCase):
    def test_scrape(self):
        scraper = Scraper(symbols)
        info, data = scraper.scrape()
        self.assertIsNotNone(data)

    def test_news(self):
        news = Newspaper(symbols)
        news.save_news_to_csv(n=5)


if __name__ == "__main__":
    unittest.main()

