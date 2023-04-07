from concurrent.futures import ThreadPoolExecutor

def fn(name,age):
    for i in range(100):
        print(name,i,age)

if __name__ == "__main__":
    # 创建线程池
    with ThreadPoolExecutor(50) as t:  # 里边可以存储50个线程
        for i in range(100):
            t.submit(fn,name = f'线程{i}',age = 10)

    # 等待线程池中的任务结束才能继续执行
    print('结束了')