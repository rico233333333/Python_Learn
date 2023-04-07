import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("工具栏")
        self.q_tool_bar()
        self.show()

    def q_tool_bar(self):
        tool = QToolBar(self)
        a = tool.addAction("攻击以")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
