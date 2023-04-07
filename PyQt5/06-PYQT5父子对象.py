# 06-PYQT5父子对象
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置父子对象")  # 此处设置对象窗口名称
        self.resize(500, 500)  # 此处设置窗口大小
        self.txt()  # 此处设置子对象
        # self.QObject对象父子关系操作()
        self.QObject对象父子关系图()
        # self.QObject对象父子关系操作()
        self.show()  # 此处调用布局管理器，把对应的组件放置到主窗口当中

    # 此处设置子对象实例方法
    def txt(self):
        label01 = QLabel(self)  # 此处切记传参
        label01.setStyleSheet("font-size:30px;color:red;")
        label01.setText("草拟吗的批")  # 设置Label文本参数
        label01.move(200, 200)  # 设置Label文本位置

    # 此处创建父子对象实例方法
    def QObject对象父子关系操作(self):
        obj1 = QObject()
        obj2 = QObject()
        print(obj1)  # 输出obj1的内存地址
        print(obj2)  # 输出obj2的内存地址
        # 设置父对象
        # 格式是
        # 子.setParent(父) 设置括号里面的为括号外的父对象
        # 设置obj1为obj2的子对象
        obj1.setParent(obj2)
        print(obj1.parent())  # 打印obj1父对象的父对象的属性

    # 构建父子关系图
    def QObject对象父子关系图(self):
        """obj0 = QObject()
        print(obj0)
        obj1 = QObject()
        obj1.setObjectName("1")  # 给obj1设置name属性为 1
        obj2 = QObject()
        obj2.setObjectName("2")  # 给obj2设置name属性为2
        obj3 = QObject()
        obj3.setObjectName("3")  # 给obj3设置name属性为3
        obj4 = QObject()
        obj5 = QObject()
        # 分别设置obj0为obj1和obj2的父对象
        obj1.setParent(obj0)  # 设置obj0为obj1的父对象
        print(obj1)
        print(obj1.parent())
        obj2.setParent(obj0)  # 设置obj0为obj2的父对象
        print(obj2)
        print(obj2.parent())
        # 设置obj3为obj1的子对象
        obj3.setParent(obj1)
        print(obj1)
        print(obj3)
        print(obj3.parent())
        # 设置obj2为obj4、obj5的父对象
        obj4.setParent(obj2)
        print(obj2)
        print(obj4)
        print(obj4.parent())
        obj5.setParent(obj2)
        print(obj2)
        print(obj5)
        print(obj5.parent())
        # print(":^25{}".format("ajkshdjkhakjh"))  # 格式化输出字符串忘记
        # .children() 输出所有的直接子对象(不包括间接)
        # 输出obj0的所有直接子对象
        print(obj0.children())  # 输出父对象所有的直接子对象 返回值是一个列表
        # 输出obj1的所有子对象
        print(obj1.children())
        # 输出obj2的所有子对象
        print(obj2.children())

        # 按照条件输出一个子对象
        # 设置一个label标签作为QObject的子对象
        # lab02 = QLabel()
        # lab02.setParent(obj0)  # 不能有此父子对象因为QObject是不可建的一个对象 QLabel 是一个可建的文本标签 在QObject上无法显示
        # print("189273908",obj0.findChild())

        # 设置findChild的三个参数
        print(obj0.findChild(QObject))  # 当只有一个参数时只会输出第一个标签对应的子对象(只输出一个子对象)
        print(obj0.findChild(QObject, "2"))  # 输出所有QObject标签下的setObjectName的值为2的子对象(只输出一个)
        print(obj0.findChild(QObject, "3", Qt.FindChildrenRecursively))  # 默认递归遍历Qt.FindChildrenRecursively
        print(obj0.findChild(QObject, "2", Qt.FindDirectChildrenOnly))  # 仅限于子对象，只查找子对象

        # 查找多个对象findChildren()
        print(obj0.findChildren(QObject))  # 查找QObject标签下的所有子对象
        print(obj0.findChildren(QObject, "2" , Qt.FindDirectChildrenOnly))"""

        # 新建obj1、obj2
        obj1 = QObject()
        obj2 = QObject()

        # 创建指针指向obj1
        self.obj1 = obj1  # 这样就不会被释放掉了

        # 设置obj1为obj2的父对象
        obj2.setParent(obj1)

        # 监听obj2对象是否被释放
        obj2.destroyed.connect(lambda: print("obj2被释放"))

        # 释放obj1
        del self.obj1  # 释放父对象子对象也会跟着被释放


if __name__ == '__main__':
    # 此处调用创建的主窗口类
    app = QApplication(sys.argv)
    window = Window()  # 此处不需要传入参数
    sys.exit(app.exec_())  # 设置事件循环
