import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.myhome.ie/residential/cavan/property-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
listings = soup.find("div", class_="PropertyListingCard__PropertyInfo")
#print(listings)

#price = listings.find(class_="PropertyListingCard__Price").text
#print(price)

#address = listings.find(class_="PropertyListingCard__Address").text
#print(address)

for listing in listings:
    entry = []

    price = listings.find(class_="PropertyListingCard__Price").text
    entry.append(price)

    address = listings.find(class_="PropertyListingCard__Address").text
    entry.append(address)

    print(entry)