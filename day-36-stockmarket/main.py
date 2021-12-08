import requests
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "A4TQNQILZ7UZDBB0"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "e624658b4083442e8f7a5130d857dd95"

TWILIO_SID = 'AC41e68ae177f91dce73a28a3756dde6b9'
TWILIO_AUTH_TOKEN = '8536ac1cace0a5a0e5b9a1b196fb5ea2'

# NEWS_API_KEY = NewsApiClient(api_key='e624658b4083442e8f7a5130d857dd95')  1


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

dif_percent = round((difference / float(yesterday_closing_price))) * 100
print(dif_percent)

if abs(dif_percent) >= 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)


    formatted_articles = [f"{STOCK_NAME}: {up_down}{dif_percent}%\nHeadline: {article['title']}. \nBrief:{article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+14432513193",
            to="+4012345"
        )









# articles = NEWS_API_KEY.get_everything(q=COMPANY_NAME)["articles"][:3]    1
#
# first_article_title = articles[0]["title"]
# first_article_content = articles[0]["content"]
# second_article_title = articles[1]["title"]
# second_article_content = articles[1]["content"]
# third_article_title = articles[2]["title"]
# third_article_content = articles[2]["content"]        1



    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 





