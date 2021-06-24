import requests
import lxml
from bs4 import BeautifulSoup

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

print(product_price)
