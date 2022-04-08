import requests 
from bs4 import BeautifulSoup as BS


page = 1
namber = 1

while True:

    url = requests.get('https://stopgame.ru/review/new/izumitelno/p' + str(page))

    html = BS(url.content, "html.parser")
    items = html.select(".items > .article-summary")
    if(len(items)):
        for el in items:
            namber += 1
            title = el.select(".article-description > .caption > a")
            for link in title:
                links = link.get('href')
                print( str(namber) + title[0].text)
                print("https://stopgame.ru"+ str(links))
                print("=======================================")


    else:
        break
    page += 1
