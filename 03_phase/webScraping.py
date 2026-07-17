import requests

from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response  = requests.get(url)

# Raw HTML
#       │
#       ▼
# BeautifulSoup
#       │
#       ▼
# Search HTML easily

soup  =BeautifulSoup(response.text, "html.parser")

title =soup.find("h1")
print(title.text)

# finding multiple elements

paragraph = soup.find_all('p')

# for para in paragraph:
#     print(para.text)



# extract all the quotes

quotes = soup.find_all('span' , class_="text")

# for quote in quotes:
#     print(quote.text)

authors = soup.find_all("small", class_="author")

for auth in authors:
    print(auth.text)

# print(soup)

# print(response.text)