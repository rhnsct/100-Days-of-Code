import requests
import os
from newsapi import NewsApiClient
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_Endpoint = "https://www.alphavantage.co/query"
alpha_vantage_api_key = "9QO720PYBOB78JOP"

NEWS_Endpoint = "https://newsapi.org/v2/everything"
news_api_key = os.environ.get("NEWS_API_KEY")
news_api = NewsApiClient(api_key=news_api_key)

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
sender_number = "+NUMBER"
receiver_number = "+NUMBER"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key,  
}


def get_price_dif():
    response_av = requests.get(url=AV_Endpoint, params=stock_parameters)
    response_av.raise_for_status()
    
    price_data = response_av.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in price_data.items()]
    yesterday_close = float(data_list[0]["4. close"])
    before_yesterday_close = float(data_list[1]["4. close"])
    
    percent_dif_close = (((yesterday_close - before_yesterday_close) / before_yesterday_close) * 100)
    rounded_percentage = round(percent_dif_close, 2)
    return rounded_percentage


# Get most recent and relevant headlines
top_headlines = news_api.get_everything(
    qintitle=COMPANY_NAME, page_size=3, language='en', page=1, sort_by="publishedAt")

articles = [item for item in top_headlines["articles"]]

# Write article headline/url/date
headline_url = ""

for item in articles:
    article_date = item['publishedAt'].split('T')[0]
    headline_url += f"\n\nHeadline: {item['title']}\nURL: {item['url']}\nArticle Date: {article_date}"


stock_price = get_price_dif()

# Different messages depending on if the stock is depreciating or growing in price
if stock_price > 0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{STOCK}: 🔺{stock_price}%{headline_url}",
        from_=sender_number,
        to=receiver_number
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{STOCK}: 🔻{abs(stock_price)}%{headline_url}",
        from_=sender_number,
        to=receiver_number
    )


