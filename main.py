from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.imdb.com/chart/top'

try:
  page = requests.get(url)
  print(page.raise_for_status())

  soup = BeautifulSoup(page.text, 'html.parser')

  sections = soup.find('tbody', class_ = 'lister-list').find_all('tr')

  L = []
  for section in sections:
    rank = section.find('td', class_ = 'titleColumn').text.split()[0][:-1]
    title = section.find('td', class_ = 'titleColumn').a.text
    year = section.find('span', class_ = 'secondaryInfo').text[1:-1]
    #year = section.find('td', class_ = 'titleColumn').span.text[1:-1]
    rating = section.find('td', class_ = 'ratingColumn imdbRating').strong.text
  
    info = [rank, title, year, rating]
    L.append(info)

    data = pd.DataFrame(L, columns = ['Rank', 'Title', 'Year', 'Rating'])
  print(data.head())

except Exception as e:
  print(e)