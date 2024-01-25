from bs4 import BeautifulSoup
import pandas as pd
import requests

root = 'https://subslikescript.com'
url = f'{root}/movies'
web = requests.get(url)
content = web.text

soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', {'class': 'main-article'})

links = []

for link in box.find_all('a', href=True):
    links.append(link['href'])

titles = []
plots = []
movies_dict = {'Titles':titles, 'Plots':plots}

for link in links:
    url = f'{root}/{link}'
    web = requests.get(url)
    content = web.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', {'class': 'main-article'})

    title = box.find('h1').get_text()
    titles.append(title)
    try:
        plot = box.find('p', class_="plot").get_text()
        plots.append(plot)
    except:
        plot = "Empty"
        plots.append(plot)

df = pd.DataFrame.from_dict(movies_dict)
print(df)
