import sys
import PyQt5.QtCore as QtCore
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("这是一个窗口")
        self.resize(400, 300)
        self.setStyleSheet("background-color:cyan;")
        self.lineEdit_111()
        self.show()

    def lineEdit_111(self):
        lineEdit = QLineEdit(self)
        lineEdit.setAlignment(QtCore.Qt.AlignLeft)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
