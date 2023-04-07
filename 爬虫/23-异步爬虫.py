import asyncio
from asyncio import tasks
import aiohttp

urls = [
    'http://kr.shanghai-jiuxin.com/file/bizhi/20221017/utuesn5liw4.jpg',
    'http://kr.shanghai-jiuxin.com/file/bizhi/20221017/xevhtcggvd3.jpg',
    'http://kr.shanghai-jiuxin.com/file/bizhi/20221017/r4mmswwqo1a.jpg',
]

async def aiodownload(url):
    # 发送请求
    # 得到图片内容
    # 保存图片
    # 需要引入 s = aiohttp.ClientSession() >等价于> requests 
    name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:  # 二进制文件使用resp.content.read()  图片视频等  aiofiles
            with open(name,mode='wb') as f:
                f.write(await resp.content.read())  # 此处需要挂起 读取写入异步操作
    

async def main():
    tasks = []
    for i in urls:
        tasks.append(asyncio.create_task(aiodownload(i)))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())