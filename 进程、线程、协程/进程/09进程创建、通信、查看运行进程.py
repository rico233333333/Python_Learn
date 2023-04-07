import multiprocessing
import time
import os


def read_1(queue):
    print(f'读取队列函数，当前进程号为:{os.getpid()}，当前对象的主进程号为{os.getppid()}')
    for i in range(queue.qsize()):  # queue.qsize() 获取当前队列的长度
        print(f'读取到的值为{queue.get()},当前进程号为:{os.getpid()},当前父进程号为:{os.getppid()}')  # queue.get()  读取队列一次取一个


def write_1(queue):
    print(f'写入队列函数，当前进程号为:{os.getpid()}，当前对象的主进程号为{os.getppid()}')
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        queue.put(i)  # queue.put()  队列写入函数
        print(f'写入队列的的值为{i},当前进程号为:{os.getpid()},当前父进程号为:{os.getppid()}')


if __name__ == "__main__":
    print(f'子进程执行开始，当前主进程号为:{os.getppid()}')
    # 创建队列对象
    queue = multiprocessing.Manager().Queue()
    # 创建进程池对象
    pool = multiprocessing.Pool(5)  # 进程池里面放置有5个进程对象
    # 将函数对象放入到进程池里边
    pool.apply_async(write_1,(queue,))  # 此处给进程传参  参数类型为元组
    # 给进程池里对象足够的时间执行
    time.sleep(1)  # 这里休眠一秒
    # 将另一个函数也传入进程池
    pool.apply_async(read_1,(queue,))  
    pool.close()  # 关闭进程池
    pool.join()  # 清理进程浪费的进程
    print(f'子进程执行结束，当前主进程号为:{os.getppid()}')