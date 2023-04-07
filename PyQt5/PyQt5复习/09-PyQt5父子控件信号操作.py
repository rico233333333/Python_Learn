import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置主窗口标题")
        self.resize(600, 400)
        self.QObject信号操作()
        self.show()

    def QObject信号操作(self):
        self.obj = QObject()
        self.obj.objectNameChanged.connect(self.objectNameChange_cao)
        self.obj.setObjectName("改变改变")

    def objectNameChange_cao(name):
        print("对象名称发生了变化", name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
