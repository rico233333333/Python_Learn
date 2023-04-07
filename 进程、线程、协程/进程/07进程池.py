import multiprocessing
import random
import time

# 定义一个进程需要执行的函数
def work(mum):  
    time.sleep(random.randint(1,5))
    print('mum=',mum)

# 创建一个进程池 他最大可以存在3条进程可以一体执行

if __name__ == "__main__":
    pool = multiprocessing.Pool(3)

    # 向进程池中添加任务
    for i in range(10):
        pool.apply_async(work,(i,))  # pool.apply_async 向进程池中添加进程 并传参

    pool.close()
    pool.join()  # join会等待进程池中的所有子进程都结束了 在执行主进程  回收进程资源


    print('主进程添加进程结束.......')