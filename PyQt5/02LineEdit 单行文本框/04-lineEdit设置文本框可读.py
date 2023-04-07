import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置窗口标题")
        self.resize(400, 300)
        self.lineEdit_111()
        self.show()

    def lineEdit_111(self):
        lineEdit = QLineEdit(self)
        lineEdit.setStyleSheet("background-color:cyan")
        lineEdit.setText("设置只可读取不可编辑")
        lineEdit.setReadOnly(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
