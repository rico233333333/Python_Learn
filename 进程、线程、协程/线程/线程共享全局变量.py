import threading

# 定义一个全局变量
g = 0
# 定义两个函数 这是线程执行代码
def task():
    # 每次存款100元
    global g  # 此处定义全局变量
    for i in range(5):
        g = g + 100
        print('存款成功',i,g)


def task2():
    # 每次取款100元
    global g  # 此处定义全局变量
    for i in range(5):
        g = g - 100
        print('取款成功',i,g)


# 创建线程对象
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task2)
# 调用start方法 让线程开始运行
t1.start()
t2.start()

print(g)