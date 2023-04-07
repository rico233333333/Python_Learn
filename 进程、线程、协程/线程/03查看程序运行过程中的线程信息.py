import threading
import time

print(threading.enumerate())

def task_1():
    for i in range(5):
        print(i)
        time.sleep(1)

# 创建线程对象
t1 = threading.Thread(target=task_1)
t1.start()
print(threading.enumerate())  # 循环打印线程列表信息
time.sleep(6)
print(threading.enumerate())  # 六秒后再次查看线程列表信息