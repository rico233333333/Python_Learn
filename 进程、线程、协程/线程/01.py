import threading


def func():
    for i in range(1000):
        print('def', i)


if __name__ == '__main__':
    t = threading.Thread(target=func)  # 导入多线程类 创建多线程对象 给线程安排任务
    t.start()  # 开始执行多线程  告诉他可以上工了 具体执行时间由CPU决定

    for i in range(1000):
        print('main', i)
