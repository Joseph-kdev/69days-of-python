import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

BUY_PRICE = 200

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
}

response = requests.get("https://www.amazon.com/Nothing-Smartphone-Unlocked-Android-Dimensity/dp/B0CQ7P5X9N/ref=sr_1_1?crid=31IMZD1447O62&dib=eyJ2IjoiMSJ9.Bn7HfFD6WEDOXgEH2aeYJCodc4dDhYygxH6X6-ZaaMki0ZDnPdk8GPvgJtGj7Q58fvBibtXGKQDoFIQblC6nI7gdh1ZoMaRwYH8fVpmZpYJa5s7A4VODtx1ZpD6KHYHLOtzcZUkOIpbjPcueE3An2DlRSmxJPGhrz_7FsHzKjvdN3ttwWKgnWzvnIdlEmQnTr8Gqkb07ssOxO_CZYZ0Imzi6-nneoM1EXr95B2O8lZQ.g_6z3gB1CJykmmh78xtarRI-q66UugauPI1uyD1RFaA&dib_tag=se&keywords=nothing%2Bphone&qid=1723638319&sprefix=Nothin%2Caps%2C2560&sr=8-1&th=1", headers=headers)
soup = BeautifulSoup(response.text, "lxml")

product_price = soup.select("#corePriceDisplay_desktop_feature_div .a-price")
title = soup.find(id="productTitle").get_text().strip()

for product in product_price:
    price = product.getText()
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    
    
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    
    with smtplib.SMTP(YOUR_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addr=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
