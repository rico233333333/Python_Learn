import aiohttp
import asyncio
import requests
import re  # 效率提高



# 内容URL
z_url = r'https://dushu.baidu.com/api/pc/getChapterContent?data={book_id:4306063500,cid:4306063500|1569782244,need_bookinfo:1}'

def getcatalog(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text

#页面解析函数
def main_page(html_text):
    re.compile(r'(?<=<dd>\s).*(?=</dd>s\\)')

async def main():
    # 章节URL
    url = r'https://www.17k.com/list/3479827.html'
    url_z = getcatalog(url=url)
    print(url_z)

if __name__ == '__main__':
    asyncio.run(main())
