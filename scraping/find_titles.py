from urllib.request import urlopen
from bs4 import BeautifulSoup
# import re
# from lxml import etree

# # url = 'http://example.com'
# page = urlopen(url)
# html_code = page.read().decode('utf=8')
# # start = html_code.find('href="') + 6
# # end = html_code.find('">More')
# # link = html_code[start: end]
# # link = r'(https?://\S+)(?=")'
# # print(re.findall(link, html_code))
#
# tree = etree.HTML(html_code)
# for i in range(3):
#     path = '//*[@id="post-15271"]/div[2]/a/h2/text()'.format()
#     print(tree.xpath(path))
#
# # /html/body/main/section[3]/div/div/article[1]/div[2]/a/h2\
# # //*[@id="post-15195"]/div[2]/a/h2
#
#
# # res = requests.get(url)
# # soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup)


## 1. Напишите программу для получения названий последних статей из блога:

url = 'https://www.oreilly.com/radar/'
page = urlopen(url)
html = page.read().decode('utf=8')
soup = BeautifulSoup(html, "html.parser")
titles = set()
for title in soup.find_all(class_='post-title'):
    if title != None:
       titles.add(title.get_text())

for title in titles:
    print(title)

if __name__ == '__main__':
    pass