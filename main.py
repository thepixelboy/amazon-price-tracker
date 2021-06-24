import requests
import lxml
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

TARGET_PRICE = 150

page_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept-Language": "en-US,en;q=0.5",
}

product_page = input("Insert a product page to check price for: ")
response = requests.get(product_page, headers=page_headers)
website_html = response.text
soup = BeautifulSoup(website_html, "lxml")

# Get the product price (without currency symbol) as a float
product_price = float(soup.find(name="span", id="priceblock_ourprice").getText().split("$")[1])
product_name = soup.find(name="span", id="productTitle").getText().strip()

if product_price < TARGET_PRICE:
    message = f"{product_name} is now {product_price}"

    with smtplib.SMTP(os.getenv("SMTP_SERVER"), port=os.getenv("SMTP_PORT")) as connection:
        connection.starttls()
        result = connection.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("EMAIL_ADDRESS"),
            to_addrs=os.getenv("EMAIL_PASSWORD"),
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_page}",
        )
