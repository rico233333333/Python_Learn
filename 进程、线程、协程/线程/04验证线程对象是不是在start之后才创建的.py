import threading
import time

print(threading.enumerate())  # 打印线程列表 enumerate() 以列表的形式呈现线程信息函数

def task_1():
    for i in range(5):
        print(i)
        time.sleep(1)

# 创建线程对象
t1 = threading.Thread(target=task_1)  
print(threading.enumerate())
t1.start()
print(threading.enumerate())
time.sleep(6)
print(threading.enumerate())