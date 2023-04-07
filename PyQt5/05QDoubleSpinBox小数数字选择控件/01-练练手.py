from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox小数数字选择控件")
        self.resize(1000, 500)
        self.double_spin_box()
        self.show()

    def double_spin_box(self):
        qdouble_spin_box = QDoubleSpinBox(self)
        qdouble_spin_box.setDecimals(3)  # 设置小数位数
        qdouble_spin_box.setValue(0.001)  # 设置初始值
        qdouble_spin_box.setRange(0, 99.999)  # 设置小数的取值范围
        qdouble_spin_box.setSingleStep(0.001)  # 设置步长值
        qdouble_spin_box.resize(100, 50)
        qdouble_spin_box.setStyleSheet("font-size:20px")
        label111 = QLabel(self)
        label111.move(0, 50)
        label111.setStyleSheet("font-size:20px")
        label111.setText("QDoubleSpinBox的值为："+str(qdouble_spin_box.value()))

        def double_str():
            label111.setText("QDoubleSpinBox的值为："+str(qdouble_spin_box.value()))

        qdouble_spin_box.valueChanged.connect(double_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
