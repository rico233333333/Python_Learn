from threading import Thread


class Run(Thread):
    def run(self):
        for i in range(1001):
            print('子线程', i)


if __name__ == '__main__':
    r = Run()
    r.start()
    for i in range(1001):
        print('主线程', i)
