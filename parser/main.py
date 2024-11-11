import json

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'

list_obj = []

for number in range(1, 11):
    page = requests.get(url+f'/page/{number}')

    dic_filteredNews = {}
    allNews = []

    list_news = []

    soup = BeautifulSoup(page.text, 'html.parser')

    allNews = soup.findAll('div', {'class': 'quote'})

    for data in allNews:
        filteredNews = {}
        if data.find('a') is not None:
            link = data.find('a')['href']
            filteredNews[
                data.text.replace('\n', '').replace('\u201c', '').replace('\u201d', '').replace('\u00e9', '').replace('\u2032', '')
            ] = url+link

            list_obj.append(filteredNews)

json_obj = json.dumps(list_obj, ensure_ascii=False, indent=4)

with open('my.json', 'a') as f:
    f.write(json_obj)
