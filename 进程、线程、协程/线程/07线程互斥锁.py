import threading

# 创建一个全局变量来存储互斥锁 实例对象
m1 = threading.Lock()

# 创建一个全局变量
glab_num = 0

# 定义两个函数
def gl1(num):
    global glab_num
    for i in range(num):
        m1.acquire()  # 上锁
        glab_num += 1
        m1.release()  # 解锁
    print('线程1：',glab_num)


def gl2(num):
    global glab_num
    for i in range(num):
        m1.acquire()  # 上锁
        glab_num += 1
        m1.release()  # 解锁
    print('线程2：',glab_num)


# 创建线程对象
t1 = threading.Thread(target=gl1,args=((100000000,)))
t2 = threading.Thread(target=gl2,args=((100000000,)))

t1.start()  # 执行代码
t2.start()