# Stock News Alert System

This Python script fetches stock price data from Alpha Vantage, relevant news articles from News API, and sends an alert message using Twilio based on the stock's percentage change.

## Prerequisites
- Alpha Vantage API key
- News API key
- Twilio account SID and authentication token
- Twilio phone numbers (sender and recipient)

## Libraries Used
- `datetime`: to handle date and time operations
- `requests`: for making HTTP requests to APIs
- `twilio.rest`: Twilio REST API client for sending SMS alerts

## Setup
1. Replace placeholders for `STOCK_API_KEY`, `NEWS_API_KEY`, `account_sid`, `auth_token`, "phone number from twilio", and "your phone number" with your actual API keys and phone numbers.
2. Install required libraries using `pip install requests twilio`.

## Steps
1. **Fetch Stock Data:**
   - Utilizes Alpha Vantage API to get daily time series stock data for a specified stock symbol (e.g., TATAMOTORS.BSE).
   - Calculates the percentage change in stock price between yesterday and the day before yesterday.

2. **Fetch News Articles:**
   - Uses News API to retrieve recent news articles related to the specified company name (e.g., TATA MOTORS).
   - Filters articles in English from the past 7 days and sorts them by relevancy.
   - Limits the number of articles to 3.

3. **Send SMS Alert:**
   - Chooses an emoji symbol ("🔺" or "🔻") based on the stock's percentage change.
   - Constructs a message with the stock symbol, percentage change, headline, and brief of each news article.
   - Sends SMS alerts using the Twilio API to the specified recipient's phone number.

## Usage
Run the script, and it will provide the percentage change in the stock price and send an SMS alert with relevant news information.

Note: Ensure that you comply with API usage guidelines for Alpha Vantage, News API, and Twilio.

Feel free to customize the script based on your requirements and integrate additional functionalities.
