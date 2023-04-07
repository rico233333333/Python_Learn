import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置窗口标题")
        self.resize(400, 300)
        self.label111()
        self.show()

    def label111(self):
        label1 = QLabel(self)
        label1.setText("这是一个案例演示文本")  # 设置label标签文本哟
        label1.resize(400, 250)
        label1.setStyleSheet("background-color:cyan;font-size:20px;color:red")  # 设置label标签的背景、字体大小、颜色
        # 默认左对齐 也可以设置
        label1.setAlignment(QtCore.Qt.AlignLeft)  # 设置文本左对齐


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
