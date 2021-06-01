from bs4 import BeautifulSoup
import requests

url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

name1 = soup.find_all('p', class_='selection-film-item-meta__name')
original1 = soup.find_all('p', class_='selection-film-item-meta__original-name')
rating1 = soup.find_all('span', class_='rating__value rating__value_positive')
country1 = soup.find_all('span', class_='selection-film-item-meta__meta-additional-item')

out = []
out2 = []
out3 = []

for m in range(0, len(original1)):
    out.append(original1[m].text)
for k in range(0, len(out)):
    out2.append(out[k].split(', '))
for y in range(0, len(out2)):
  if len(out2[y]) == 1:
    out2[y].insert(0,'')
for i in range(0, len(name1)):
    out3.append('Название: ' + name1[i].text + '\n' + 'Оригинальное название: ' + out2[i][0] + '\n' + 'Год: ' + out2[i][
        1] + '\n' + 'Страна: ' + country1[::2][i].text + '\n' + 'Жанр: ' + country1[1::2][i].text + '\n' + 'Оценка: ' +
                rating1[i].text + '\n')

for t in range(0, len(out3)):
    print("".join(out3[t]))


url = 'https://www.kinopoisk.ru/lists/top250/anime/?tab=all'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

name1 = soup.find_all('p', class_='selection-film-item-meta__name')
original1 = soup.find_all('p', class_='selection-film-item-meta__original-name')
rating1 = soup.find_all('span', class_='rating__value rating__value_positive')
country1 = soup.find_all('span', class_='selection-film-item-meta__meta-additional-item')

out = []
out2 = []
out3 = []

for m in range(0, len(original1)):
    aut.append(original1[m].text)
for k in range(0, len(out)):
    out2.append(out[k].split(', '))
for i in range(0, len(name1)):
    out3.append('Название: ' + name1[i].text + '\n' + 'Оригинальное название: ' + out2[i][0] + '\n' + 'Год: ' + out2[i][
        1] + '\n' + 'Страна: ' + country1[::2][i].text + '\n' + 'Жанр: ' + country1[1::2][i].text + '\n' + 'Оценка: ' +
                rating1[i].text + '\n')

for t in range(0, len(out3)):
    print("".join(out3[t]))