from base64 import encode
import requests
import aiohttp
import asyncio

def text():
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    
    resp = requests.get(url,headers=header)

    return resp.json()['data']['novel']['items']

def url_h(text):
    url_list = []
    for i in text:
        i['title']
        i['price_status']
        i['cid']
        z_url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|'+i['cid']+'","need_bookinfo":1}'
        url_list.append(z_url)
    return url_list

# 异步爬虫定义
async def Z_json(text_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(text_url) as resp:
            dic = await resp.json()
            # print(await resp.json()['data']['novel']['chapter_title'])  # type: ignore
            with open('C:/Users/RicardoCohen/Desktop/爬取小说/{}.txt'.format(dic['data']['novel']['chapter_title']) ,mode='w',encoding='utf8') as w:
                w.write(dic['data']['novel']['content'])
                
# 异步函数定义 async
async def z_text():
    tasks = []
    for i in url_h(text()):
        tasks.append(asyncio.create_task(Z_json(i)))
        print(i)
    await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(z_text())
