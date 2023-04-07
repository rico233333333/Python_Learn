import multiprocessing
import time

def task1(q):
    for i in ['A','B','C','D']:
        q.put(i)

def task2(q):
    while True:
        time.sleep(0.5)
        if not q.empty():  # q.empty() 判断队列是否为空 为空返回True 
            value = q.get()
            print('取出来的数据是：',value)
        else:
            print('没有数据了')
            break


if __name__ == "__main__":
    # 创建进程队列对象
    q = multiprocessing.Queue()  # 此处没有约定存储数量

    # 创建进程对象
    p1 = multiprocessing.Process(target=task1,args=(q,))
    p2 = multiprocessing.Process(target=task2,args=(q,))

    # 启动子进程
    p1.start()
    p2.start()