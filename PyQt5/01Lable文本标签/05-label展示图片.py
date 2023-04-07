import sys

from PyQt5 import QtCore
from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap  # 导入图片类


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("这是窗口标题")
        self.resize(2400, 1300)  # x,y 如此设置
        self.setStyleSheet("background-color:cyan;")
        self.label11()
        self.show()

    def label11(self):
        label1 = QLabel(self)
        label1.setPixmap(QPixmap(r'D:\CODE\python_project\src\PyQt5\01Lable文本标签\img\delivery-4568738.png'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
