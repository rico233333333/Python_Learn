import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget事件机制的学习")
        self.resize(500, 700)  # 设置窗口大小  500代表X轴 700代表Y轴
        self.setup_gui()
        self.show()

    def setup_gui(self):
        pass

    def showEvent(self, QShowEvent):
        print("窗口被展示出来了")

    def closeEvent(self, QCloseEvent):
        print("窗口被关闭了")

    def moveEvent(self, QMoveEvent):
        print("窗口移动了")

    def resizeEvent(self, QResizeEvent):
        print("窗口尺寸大小大小改变了")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
