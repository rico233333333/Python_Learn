from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("对象删除")
        self.resize(600, 700)  # 设置窗体大小
        self.QObject对象删除操作()
        self.show()  # 将对象写入窗体

    def QObject对象删除操作(self):
        # 构建一个树
        qob1 = QObject()
        self.qob1 = qob1
        qob2 = QObject()
        qob3 = QObject()

        # 3是2的子对象 2是1的子对象
        qob3.setParent(qob2)
        qob2.setParent(qob1)

        qob1.destroyed.connect(lambda: print("对象被释放了"))
        qob2.destroyed.connect(lambda: print("对象被释放了"))
        qob3.destroyed.connect(lambda: print("对象被释放了"))
        qob2.deleteLater()  # 稍后删除对象 对象还存在在内存之中 还在使用对象qobj2
        print(qob2.children())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
