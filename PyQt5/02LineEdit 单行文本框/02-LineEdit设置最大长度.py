import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("这是一个窗口")
        self.resize(400, 300)
        self.lineEdit_1()
        self.show()

    def lineEdit_1(self):
        lineEdit_11 = QLineEdit(self)
        lineEdit_11.setText("不错不错")
        lineEdit_11.setPlaceholderText("请输入")
        lineEdit_11.setMaxLength(32)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
