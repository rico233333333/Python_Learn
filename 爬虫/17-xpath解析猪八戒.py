import requests
from lxml import etree

url = 'https://list.gome.com.cn/cat10000145.html?intcmp=sy-1000052897-1'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

resp = requests.get(url=url)

print(resp.text)

page = etree.HTML(resp.text)

page_ul = page.xpath('/html/body/div[10]/div/div[2]/div[3]/ul')  # 此处返回内存地址  会以列表包裹起来

page_li = page_ul[0].xpath('./li')

print(page_li)

for data in page_li:  # /html/body/div[10]/div/div[2]/div[3]/ul/li[1]/div/div/div[2]/p/span
    yuan = data.xpath('./div/p[class="item-name"]/text()')
    print(yuan)
