import sys  # 导入sys库
from PyQt5.Qt import *  # 导入PyQt5.Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("父子对象测试")
        self.resize(600, 800)
        # 此处写入方法实例
        self.QObject信号操作()
        self.show()

    def QObject信号操作(self):
        self.obj = QObject()
        # destoryed.connect(方法)
        """def destory_cao(obj):
            print("对象被释放", obj)
        
        self.obj.destroyed.connect(destory_cao)

        del self.obj"""
        # objectNameChanged()
        def objectNameChanged_cao(name):
            print("对象名称发生改变", name)
        self.obj.objectNameChanged.connect(objectNameChanged_cao)
        self.obj.setObjectName("改变了吧")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
