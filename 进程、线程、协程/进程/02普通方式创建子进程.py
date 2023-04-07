import multiprocessing
import time

def temp():
    for i in range(10000):
        print('这是个子进程对象')

if __name__ == "__main__":
    # 创建子进程对象
    mul = multiprocessing.Process(target=temp)
    mul.start()
    for i in range(10000):
        print('我是主线程')