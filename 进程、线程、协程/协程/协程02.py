import asyncio

async def func():  # 创建协程函数
    print('你好啊，伞兵')
    await asyncio.sleep(3)  # 挂起
    print('嗯嗯，你好啊伞兵1号')

async def func01():  # 创建协程函数
    print('你好啊伞兵2号')
    await asyncio.sleep(3)  # 此处挂起
    print('好啊，伞兵2号')

async def main():
    # 第一中写法  不推荐
    # f1 = func()
    # f2 = func01() 
    # await f1
    # await f2

    # 第二种操作 推荐
    tasks = [
        func(),
        func01()
    ]

    await asyncio.wait(tasks)  # 切记 前面必须添加await


if __name__ == "__main__":
    asyncio.run(main())