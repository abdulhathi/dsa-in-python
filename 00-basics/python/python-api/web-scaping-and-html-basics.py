# 
# ^ pip3 install bs4
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/IBM'
headers = {"User-Agent": "MyAppName/1.0 (https://example.com/contact)"}
response = requests.get(url, headers=headers)

html_content = response.text
# print(html_content)

soup = BeautifulSoup(html_content, 
                     'html.parser')

print(html_content[:500])

links = soup.findAll('a')

for link in links:
  print(link.text)

tables = soup.findAll('table')
table_tr = tables[0].find_all(name='tr')

for i,row in enumerate(table_tr):
  # print(i, row)
  cells = row.find_all('td')
  for j, cell in enumerate(cells):
    print(j, cell)