import pandas as pd
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time
import requests

class Newspaper:
    def __init__(self, tickers):
        self.tickers = tickers if isinstance(tickers, list) else [tickers]
        self.finviz_url = 'https://finviz.com/quote.ashx?t='

    def get_news(self, n=1):
        news_data = []
        headers = {'User-Agent': 'Mozilla/5.0'}

        for ticker in self.tickers:
            url = self.finviz_url + ticker
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                html = response.content
                soup = BeautifulSoup(html, 'html.parser')
                news_table = soup.find(id='news-table')

                if news_table:
                    df_tr = news_table.findAll('tr')
                    for i, table_row in enumerate(df_tr):
                        a_tag = table_row.a
                        a_text = a_tag.text
                        a_link = a_tag['href']
                        a_link = a_link.replace('https://finviz.com/', '')  # Remove the base URL
                        td_text = table_row.td.text.strip()
                        news_data.append([ticker, a_text, a_link, td_text])
                        if i == n - 1:
                            break
            else:
                print(f"Failed to retrieve data for {ticker}. Status code: {response.status_code}")
            
            time.sleep(5)  # Add a delay of 5 seconds between requests

        return news_data

    def get_overall_sentiment(self, n=1):
        news_data = self.get_news(n=n)
        parsed_news = []

        for entry in news_data:
            ticker, headline, link, date_time = entry
            date_scrape = date_time.split()
            if len(date_scrape) == 1:
                time = date_scrape[0]
                date = None
            else:
                date = date_scrape[0]
                time = date_scrape[1]
            parsed_news.append([ticker, date, time, headline, link])
        
        analyzer = SentimentIntensityAnalyzer()
        columns = ['Ticker', 'Date', 'Time', 'Headline', 'Link']
        news_df = pd.DataFrame(parsed_news, columns=columns)
        scores = news_df['Headline'].apply(analyzer.polarity_scores).tolist()
        df_scores = pd.DataFrame(scores)
        news_df = news_df.join(df_scores, rsuffix='_right')
        mean_sentiment = round(news_df['compound'].mean(), 2)
        return mean_sentiment, news_df

    def save_news_to_csv(self, n=1, filename='src/data/news.csv'):
        news_data = self.get_news(n=n)
        analyzer = SentimentIntensityAnalyzer()
        
        parsed_news = []
        for entry in news_data:
            ticker, headline, link, date_time = entry
            date_scrape = date_time.split()
            if len(date_scrape) == 1:
                time = date_scrape[0]
                date = None
            else:
                date = date_scrape[0]
                time = date_scrape[1]
            parsed_news.append([ticker, date, time, headline, link])
        
        columns = ['Ticker', 'Date', 'Time', 'Headline', 'Link']
        news_df = pd.DataFrame(parsed_news, columns=columns)
        scores = news_df['Headline'].apply(analyzer.polarity_scores).tolist()
        df_scores = pd.DataFrame(scores)
        news_df = news_df.join(df_scores, rsuffix='_right')
        
        news_df.to_csv(filename, index=False)


