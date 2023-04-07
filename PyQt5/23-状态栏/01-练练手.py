import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("状态栏")
        self.q_statusBar()
        self.show()

    def q_statusBar(self):
        # 定义Label标签
        lab_statubar = QLabel()
        lab_statubar.setText("版权所有：RS工作室")
        # 导入状态栏控件
        q_statusBar = QtWidgets.QStatusBar(self)
        self.setStatusBar(q_statusBar)  # 装入状态栏

        q_statusBar.addPermanentWidget(lab_statubar)
        q_statusBar.showMessage("这是一条临时信息:like",0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
