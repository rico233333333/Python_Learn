import sys

from PyQt5 import QtCore
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("这是窗口标题")
        self.resize(500, 400)  # x,y 如此设置
        self.setStyleSheet("background-color:cyan;")
        self.label11()
        self.show()

    def label11(self):
        label1 = QLabel(self)
        label1.setText("<a href='https://www.baidu.com'> 百度一下你就得到 </a>")
        label1.setOpenExternalLinks(True)
        label1.setStyleSheet("background-color:yellow;color:green;font-size:20px")
        label1.resize(300, 200)
        # 设置Lambda顶端左对齐
        label1.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # 设置Label标签换行
        label1.setWordWrap(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
