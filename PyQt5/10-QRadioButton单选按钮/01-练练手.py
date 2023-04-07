import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("单选按钮")
        self.q_radio_button()
        self.show()

    def q_radio_button(self):
        q_r_b01 = QRadioButton(self)
        q_r_b01.setText("点一下")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
