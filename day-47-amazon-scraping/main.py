import requests
from bs4 import BeautifulSoup
import smtplib

headers = {"Accept-Language": "en-US,en;q=0.9,ro;q=0.8,la;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

url = "https://www.amazon.com/Acer-AN515-55-53E5-i5-10300H-GeForce-Keyboard/dp/B092YHJGMN/"
response = requests.get(url, headers=headers)


amazon_site = response.text
soup = BeautifulSoup(amazon_site, "html.parser")

price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)


title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now{price} "

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        result = connection.login("test@yahoo.ca", "aaa")
        connection.sendmail(
            from_addr="test@yahoo.ca",
            to_addrs="test@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}")






















