import threading
import time

def say(num):
    for i in range(num):
        print(i)

# 创建线程对象
t1 = threading.Thread(target=say,kwargs={'num':5})
t1.start()