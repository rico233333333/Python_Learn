from cProfile import label
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置父子对象")
        self.resize(800, 700)
        self.txt()
        self.QObject父子对象关系图()
        self.show()

    def txt(self):
        label = QLabel(self)
        label.setText("设置文本")

    def QObject父子对象关系图(self):
        obj1 = QObject()
        obj2 = QObject()
        # print("obj1的内存地址", obj1)  # 输出obj1的内存地址
        # print("obj2的内存地址", obj2)  # 输出obj2的内存地址
        # # 此处设置父子对象（obj1为obj2的父对象）
        # obj2.setParent(obj1)
        # print("obj2的内存地址（obj1的子对象）", obj2)
        # print("输出所有的子对象", obj1.children())
        # print(obj2.parent())
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()
        # 设置obj1为obj2，obj3的父对象
        # 设置obj2为obj4的父对象
        # 设置obj3为obj5的父对象
        obj2.setParent(obj1)
        obj3.setParent(obj1)
        # print(obj1.children())
        obj4.setParent(obj2)
        obj5.setParent(obj3)
        obj5.setObjectName("obj5")

        print(obj1.findChildren(QObject, "obj5"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
