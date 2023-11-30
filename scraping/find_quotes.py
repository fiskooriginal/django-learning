from urllib.request import urlopen
from bs4 import BeautifulSoup

## 2. Напишите программу, которая на основе данных таблиц создает список цитат из фильмов, выпущенных после 1995 года:
link = 'https://ru.wikipedia.org/wiki/100_%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85_%D1%86%D0%B8%D1%82%D0%B0%D1%82_%D0%B8%D0%B7_%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%B7%D0%B0_100_%D0%BB%D0%B5%D1%82_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_AFI'
page = urlopen(link)
html = page.read().decode('utf=8')
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', class_="wikitable")

dataset = [[]]
for row in table.find_all("tr"):
    rowset = []
    for column in row.find_all("td"):
        if column.get_text() != "":
            rowset.append(column.get_text()[:-1:])
    dataset.append(rowset)
for data in dataset:
    if data != [] and data[6] > '1995':
        print(data)

if __name__ == '__main__':
    pass