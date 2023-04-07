import sys
from PyQt5.Qt import *


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
        print("label标签里的文字为", label1.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
