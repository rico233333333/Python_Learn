import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置窗口标题")
        self.resize(400, 300)
        self.lineEdit()
        self.show()

    def lineEdit(self):
        lineEdit = QLineEdit(self)
        lineEdit.setText("这是一个标签")
        # lineEdit.setStyleSheet("background-color:cyan")
        lineEdit.setFocus(True)
        lineEdit2 = QLineEdit(self)
        lineEdit2.move(0, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
