from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("创建一个窗口")
        self.resize(500, 400)
        self.qwidget()
        self.show()

    def qwidget(self):
        window1 = QWidget(self)
        window1.resize(200, 300)
        window1.setStyleSheet("background-color:cyan;")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
