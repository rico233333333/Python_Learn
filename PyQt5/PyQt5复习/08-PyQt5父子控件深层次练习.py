import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("父窗口")
        self.resize(700, 800)
        self.setStyleSheet("background-color:cyan;")
        self.window1()
        self.but2()
        print(self.children())
        self.show()

    def window1(self):
        window = QWidget(self)
        window.resize(700, 750)
        window.setStyleSheet("background-color:black")
        self.but1()
        qlab1 = QLabel(window)
        qlab1.setStyleSheet("color:cyan;")
        qlab1.move(200, 0)
        qlab1.setText("来呀")
        qlab2 = QLabel(window)
        qlab2.setText("去你妈的")
        qlab2.setStyleSheet("color:cyan;")
        qlab2.move(200, 200)
        for i in window.findChildren(QLabel):
            i.setStyleSheet("background-color:red;color:white")
        print("12123", window.children())
        window.show()

    def but1():
        but = QPushButton(self)
        but.setText("子页按钮1")

    def but2(self):
        but = QPushButton(self)
        but.move(0, 750)
        but.setText("主页按钮2")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
