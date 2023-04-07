from turtle import title
import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.umei.cc/bizhitupian/'

resp = requests.get(url=URL)
resp.encoding = "utf8"

page = BeautifulSoup(resp.text, 'html.parser')  # 设置Html解析器

h1_list = page.find_all('h1')
h1_list.pop(0)  # 移除第一个元素 第一个元素无用

h1_obj = re.compile(r'<h1>(?P<title>.*?)<small><a href="(?P<url>.*?)">更多&gt;&gt;</a></small></h1>', re.S)  # 匹配换行符

h1_dict = {}

for h1 in h1_list:
    for item in h1_obj.finditer(str(h1)):  # 此处进行类型强制转换 把bs4类型数据转换为str
        h1_dict[item.group('title')] = r'https://www.umei.cc/' + item.group('url')  # 此处格式化请求链接

# 初筛结束 二次开始

data = {
    "next": 1,
    "table": 'news',
    "action": 'getmorenews',
    "limit": 10,
    "small_length": 120,
    "classid": 69
}

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36x-requested-with: XMLHttpRequest'
}
for son_url_number in range(len(h1_dict)):
    name = list(h1_dict.keys())[son_url_number]
    url = list(h1_dict.values())[son_url_number]
    resp_son = requests.post(url=url, data=data, headers=header)
    son_json = resp_son.json
    print(son_json)
