import yfinance as yf
import datetime
import pandas as pd
import os

class Scraper:
    def __init__(self, symbols):
        self.symbols = symbols

    def scrape(self):
        # create an empty DataFrame to store the close values
        close_data = pd.DataFrame()

        # loop through the symbols and extract the close values
        for symbol in self.symbols:
            # get the data for the last year
            end_date = datetime.date.today()
            start_date = end_date - datetime.timedelta(days=365) # assuming a year has 365 days
            data = yf.download(symbol, start=start_date, end=end_date)

            # save the data to a CSV file
            data.to_csv(f'src/data/{symbol}_data.csv')

            # extract the close values for the last year
            close_values = data['Close']

            # add the close values to the DataFrame
            close_data[symbol] = close_values

        # set the index of the DataFrame to the date
        close_data.index.name = 'Date'

        # save the DataFrame to a CSV file
        close_data.to_csv('src/data/close_values.csv')

        # calculate the percentage of changes for each symbol
        pct_changes = close_data.pct_change() * 100

        # set the first row of the pct_changes DataFrame to 0
        pct_changes.iloc[0] = 0

        # save the pct_changes DataFrame to a CSV file
        pct_changes.to_csv('src/data/pct_changes.csv')

        return close_data, pct_changes



    
