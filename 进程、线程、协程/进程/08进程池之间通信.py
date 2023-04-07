import multiprocessing
import os,time,random

def read(q):
    print(f'read启动，当前进程为：{os.getpid()},当前进程的父进程为:{os.getppid()}')
    for i in range(q.qsize()):  # 此处获取队列的长度
        print(f'read从Quque中收到消息：{q.get()}')

def write(q):
    print(f'write启动，当前进程为：{os.getpid()},当前进程的父进程为:{os.getppid()}')
    for i in 'abcdefghijklmn':
        q.put(i)

if __name__ == "__main__":
    q = multiprocessing.Manager().Queue()  # 使用Manage类中的Queue  此处创建消息队列
    po = multiprocessing.Pool(5)  # 创建进程池对象
    po.apply_async(write,(q,))  # 将函数 write添加到进程队列里边儿 并传入参数 队列q

    time.sleep(1)  # 此处代码的作用是让上面对象执行结束 然后让下面代码块从队列中读取数据

    po.apply_async(read,(q,))  # 将函数read 添加到进程池队列里边 并传入参数q

    po.close()  # 结束进程池进程 关闭进程池
    po.join()  # 等待所有进线程池程结束 释放资源
    print('子进程执行结束，资源已释放')