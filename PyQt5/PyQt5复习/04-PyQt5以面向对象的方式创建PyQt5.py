import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("以面向对象的方法创建窗口")
        self.resize(500, 400)  # 设置窗口大小 第一个代表X，第二个代表Y
        self.move(300, 200)  # 设置窗口的定位
        self.setStyleSheet("background-color:cyan")
        self.label1()
        self.show()

    def label1(self):
        label = QLabel(self)
        label.setText("这是一个label标签")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
