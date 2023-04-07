import multiprocessing
import time


class Mulpro(multiprocessing.Process):
    def run(self):  # 此处对run进行重写
        for i in range(10000):
            print('这是子进程对象')

if __name__ == "__main__":
    # 创建子进程对象
    m1 = Mulpro()
    m1.start()  # 启动子进程

    for i in range(10000):
        print('这是主进程对象')