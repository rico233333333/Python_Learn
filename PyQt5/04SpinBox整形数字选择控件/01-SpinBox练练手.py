import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置窗口标题")
        self.resize(500, 600)
        self.spinbox()
        self.show()

    def spinbox(self):
        self.spin_box = QSpinBox(self)
        self.spin_box.setValue(50)  # 设置控件的当前值
        # spin_box.setMaximum(100)  # 设置控件最大值
        # spin_box.setMinimum(0)  # 设置控件最小值
        self.spin_box.setRange(0, 99)
        self.spin_box.resize(100, 50)
        self.spin_box.setStyleSheet("font-size:35px;")
        self.label111 = QLabel(self)
        self.label111.move(0, 100)
        self.label111.setStyleSheet("font-size:40px")
        self.label111.setText("QSpinBox的当前值为："+str(self.spin_box.value()))

        def getValue():
            self.label111.setText("QSpinBox的当前值为："+str(self.spin_box.value()))
        self.spin_box.valueChanged.connect(getValue)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
