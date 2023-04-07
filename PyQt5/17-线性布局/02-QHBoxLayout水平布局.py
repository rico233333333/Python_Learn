import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("水平布局")
        self.hor()
        self.show()

    def hor(self):
        but01 = QPushButton(self)
        but01.setText("按钮1")

        but02 = QPushButton(self)
        but02.setText("按钮2")

        but03 = QPushButton(self)
        but03.setText("按钮3")

        but04 = QPushButton(self)
        but04.setText("按钮4")

        hlay = QHBoxLayout(self)
        hlay.addWidget(but01)
        hlay.addStretch(1)
        hlay.addWidget(but02)
        hlay.addStretch(1)
        hlay.addWidget(but03)
        hlay.addStretch(1)
        hlay.addWidget(but04)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
