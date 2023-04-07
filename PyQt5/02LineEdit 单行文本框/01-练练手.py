import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置窗口标题")
        self.resize(400, 300)
        self.lineEdit111()
        self.show()

    def lineEdit111(self):
        lineEdit1 = QLineEdit(self)
        lineEdit1.setText("hello")  # 此行自动在文本框中输入hello

        # 允许文本框显示文字
        lineEdit1.setPlaceholderText("请输入用户名")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
