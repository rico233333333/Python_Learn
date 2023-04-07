# import asyncio
# import time

# async def func():
#     print('第一波输出')
#     time.sleep(3)  # 此处线程处在阻塞状态
#     print('第二波输出')

# # if __name__ == "__main__":
# #     func() 

# # '''
# # 协程：当程序遇见阻塞或者其他IO操作的时候可以选择性的切换到其他任务上

# # 协程只能放在单线程条件之下
# # '''



# async def func1():
#     print('你好啊，菜狗')
#     time.sleep(3)
#     print('你好啊，菜狗二号')

# async def func2():
#     print('你好啊，菜狗三号')
#     time.sleep(4)
#     print('你好啊，菜狗四号')

# if __name__ == "__main__":
#     f1 = func1()
#     f2 = func2()
#     f3 = func()

#     tasks = [
#         f1,f2,f3
#     ]

#     # 一次性启动多个任务
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2-t1)

import time
import asyncio

async def fun01():
    print('你好，潘金莲')
    # time.sleep(3)
    # 创建异步操作代码
    await asyncio.sleep(3)  # 挂起3秒
    print('你好傻逼1号')

async def fun02():
    print('你好，潘金莲2号')
    await asyncio.sleep(1)
    print('你好憨批2号')

async def fun03():
    print('你好，潘金莲3号')
    await asyncio.sleep(3)  # 挂起3秒
    print('憨憨3号')

if __name__ == '__main__':
    f1 = fun01()
    f2 = fun02()
    f3 = fun03()

    tasks = [
        f1,f2,f3
    ]
    # 创建协程
    # 测算时间
    t1 = time.time()
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()
    print(t2-t1)