import yfinance as yf

class Scraper:
    def __init__(self, symbol):
        self.symbol = symbol

    def scrape(self):
        # get all key value pairs that are available
        ticker = yf.Ticker(self.symbol)
        info = ticker.info
        for key, value in info.items():
            print(key, ":", value)
        return info

    
