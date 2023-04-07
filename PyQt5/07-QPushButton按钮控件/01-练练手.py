import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("按钮控件")
        self.resize(500, 500)
        self.button()
        self.show()

    def button(self):
        q_push_button01 = QPushButton(self)
        q_push_button01.setText("点一下，来打我啊！！！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
