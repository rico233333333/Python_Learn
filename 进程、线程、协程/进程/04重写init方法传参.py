import multiprocessing
import time


class Mul(multiprocessing.Process):
    def __init__(self, c1) -> None:
        super().__init__()
        self.c1 = c1  # 实例化属性
    
    def run(self):
        for i in range(self.c1):
            print('这是子进程')

if __name__ == "__main__":
    mul = Mul(c1=5)
    mul.start()
    for i in range(5):
        print('这是主进程对象')