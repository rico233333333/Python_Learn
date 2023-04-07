import multiprocessing
import time

def tesk():
    for i in range(5):
        print('这是一个子进程')
        time.sleep(2)

if __name__ == "__main__":
    # 创建子进程对象
    mul = multiprocessing.Process(target=tesk)
    # 启动进程
    mul.start()
    for i in range(5):
        print('这是一个主进程对象')
        time.sleep(2)
