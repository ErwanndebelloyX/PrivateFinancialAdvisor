import pandas as pd
import streamlit as st
import os

# Load the close_values.csv file
close_values = pd.read_csv(os.path.join('src', 'data', 'close_values.csv'))

# Set the index of the close_values DataFrame to the date column
close_values.index = pd.to_datetime(close_values['Date'])

# Create a multi-select menu for the user to choose which stocks to display in the chart
default_stocks = close_values.columns[1:].tolist()
stocks_to_display = st.multiselect('Select stocks to display', close_values.columns[1:], default=default_stocks)

# Create a radio button for the user to choose whether to display the close values, percentage per day, or cumulative percentage evolution
data_to_display = st.radio('Select data to display', ['Close values', 'Percentage per day', 'Cumulative percentage evolution'])

# Create a line chart for the selected stocks and data
if data_to_display == 'Close values':
    chart_data = close_values[stocks_to_display]
elif data_to_display == 'Percentage per day':
    chart_data = close_values[stocks_to_display].pct_change().mul(100)
else:
    # Create a date input for the user to choose the start date for the cumulative percentage evolution
    start_date = st.date_input('Select start date for cumulative percentage evolution', value=close_values.index.min())

    # Calculate the cumulative percentage evolution from the start date to today
    chart_data = close_values[stocks_to_display].loc[start_date:].pct_change().add(1).cumprod().sub(1).mul(100)

st.line_chart(chart_data)

# Load the news data from the CSV file
news = pd.read_csv('src/data/news.csv')

# Create a section for each selected stock
for ticker in stocks_to_display:
    st.subheader(ticker)

    # Filter the news data for the ticker
    ticker_news = news[news['Ticker'] == ticker]

    # Display the recent news headlines with clickable links
    st.write('Recent News Headlines:')
    for index, row in ticker_news.iterrows():
        headline = row['Headline']
        date = row['Date']
        link = f"https://finviz.com/{row['Link']}"
        # Use st.markdown to render HTML with a clickable link
        st.markdown(f"[{headline}]({link}) ({date})")

    # Display the overall sentiment
    mean_sentiment = ticker_news['compound'].mean()
    st.write(f'Overall Sentiment: {mean_sentiment}')

