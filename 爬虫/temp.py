import requests
import csv
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

resp = requests.get(url=url, headers=headers)

# 设置html解析器
page = BeautifulSoup(resp.text, 'html.parser')
ol = page.find('ol', class_="grid_view")
li = ol.find_all('li')
for i in li:
    div = i.find_all('div', class_="pic")
    print(div)
