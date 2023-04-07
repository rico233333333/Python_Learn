import requests
from bs4 import BeautifulSoup
import re

URL  = "https://weather.cma.cn/web/weather/52998.html"

resp = requests.get(URL)
resp.encoding = "UTF-8"

# 解析数据 生成bs4对象
page = BeautifulSoup(resp.text,"html.parser")  # resp.text:处理数据 "html.parser":告诉bs4这就是HTML页面源代码  也是指定HTML解析器

# 拿到数据 find find_all 的使用
# find(标签,标签 = 值) 找匹配到的第一个  find(div,id = 4)
# find_all() 找一堆匹配到的

# table = page.find("div",class_ = "row mt15")  # class_ 为了避免Python关键字与标签名重复
# table = page.find("tbody",attrs={"id":"dayList"})  # 以字典的方式传参

# print(type(table))
# trs = table.find_all("div")
# for line in trs:
#     print(line)
#     print(".,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,")

table = page.find("tbody")  # 以字典的方式传参
# print(table)
td = table.find_all("tr")
for i in td:
    print(i.find_all("td"))
    print(".,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,")


