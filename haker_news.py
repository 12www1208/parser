import requests
from bs4 import BeautifulSoup as BS

url  = requests.get("https://nplus1.ru/rubric/astronomy")

html  = BS(url.content, "html.parser")

items = html.select(" #main > div > div > article")

if (len(items)):

    for el in items:
        title = el.select(" a > div > h3")
        print( title)
