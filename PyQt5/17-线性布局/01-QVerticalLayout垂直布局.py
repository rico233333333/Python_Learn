import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("垂直布局")
        self.ver()
        self.show()


    def ver(self):
        vlayout = QVBoxLayout(self)
        but01 = QPushButton(self)
        but01.setText("按钮1")
        but02 = QPushButton(self)
        but02.setText("按钮2")
        but03 = QPushButton(self)
        but03.setText("按钮3")

        vlayout.addWidget(but01)
        vlayout.addSpacing(20)
        vlayout.addWidget(but02)
        vlayout.addSpacing(20)
        vlayout.addWidget(but03)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window1 = Window()
    sys.exit(app.exec_())
