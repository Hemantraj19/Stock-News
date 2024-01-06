import datetime
import requests
from twilio.rest import Client

STOCK = "TATAMOTORS.BSE"
COMPANY_NAME = "TATA MOTORS"
STOCK_API_KEY = ""
NEWS_API_KEY = ""
account_sid = ""
auth_token = ""

# STEP 1: Use https://www.alphavantage.co
url = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
stock_data = response.json()
yesterday_date = str(datetime.date.today() - datetime.timedelta(days=1))
day_before_yesterday_date = str(datetime.date.today() - datetime.timedelta(days=2))
stock_price_yesterday = float(
    stock_data["Time Series (Daily)"][yesterday_date]["4. close"]
)
stock_price_day_before_yesterday = float(
    stock_data["Time Series (Daily)"][day_before_yesterday_date]["4. close"]
)
percent_change = (
    (abs(stock_price_yesterday - stock_price_day_before_yesterday))
    / (stock_price_yesterday + stock_price_day_before_yesterday)
) * 100
percent_change = round(percent_change, 2)
print(percent_change)

# STEP 2: Use https://newsapi.org
news_url = "https://newsapi.org/v2/everything"
news_url_parameters = {
    "q": COMPANY_NAME,
    "language": "en",
    "from": str(datetime.date.today() - datetime.timedelta(days=7)),
    "to": str(datetime.date.today()),
    "sortBy": "relevancy",
    "apiKey": NEWS_API_KEY,
    "pageSize": 3,
}
news_response = requests.get(url=news_url, params=news_url_parameters)
news_response.raise_for_status()
news_data = news_response.json()

# STEP 3: Use https://www.twilio.com
symbol = "🔺" if (stock_price_yesterday - stock_price_day_before_yesterday) > 0.0 else "🔻"
client = Client(account_sid, auth_token)

for news in news_data["articles"]:
    headline = news["title"]
    brief = news["description"]
    message_body = f"{COMPANY_NAME}: {symbol}{percent_change}%\nHeadline: {headline}.\nBrief: {brief}"
    message = client.messages.create(
        body=message_body,
        from_="phone number from twilio",
        to="your phone number",
    )
    print(message.status)
