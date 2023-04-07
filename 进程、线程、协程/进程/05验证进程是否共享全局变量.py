import multiprocessing
import time

MUM = 100

def task():
    global MUM
    NUM = 200  # 修改全局变量的值
    print(MUM)


def task2():
    print('task2：',MUM)  # 打印全局变量的值

if __name__ == "__main__":
    mul = multiprocessing.Process(target=task)  # 创建子进程对象
    mul2 = multiprocessing.Process(target=task2)  # 创建子进程对象
    '''
    效果验证 若是mul2 打印出来是200证明共享全局变量
    如果没有 那就不共享全局变量
    '''
    mul.start()  # 启动子线程  
    time.sleep(1)
    mul2.start()  # 启动子线程