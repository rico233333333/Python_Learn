from concurrent.futures import ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name,i)

if __name__ == "__main__":
    # 创建进程池
    with ProcessPoolExecutor(50) as p:
        for i in range(100):
            p.submit(fn, name = f'线程{i}')
    
    print('进程结束')