from cProfile import label

from cv2 import line
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("DLC数字控件选择")
        self.resize(500, 500)  # x,y
        self.lcd_number()
        self.show()

    def lcd_number(self):
        lcd_number_class = QLCDNumber(self)
        lcd_number_class.setDigitCount(8)  # 控制选择数字的数量
        lcd_number_class.setMode(lcd_number_class.Dec)  # 设置10进制显示
        lcd_number_class.setSegmentStyle(lcd_number_class.Flat)
        lcd_number_class.resize(260, 60)
        lcd_number_class.setStyleSheet("font-size:40px")

        line_text = QLineEdit(self)
        line_text.setPlaceholderText("请在此处输入8位整数数字")  # 此处设置悬浮文本
        line_text.setMaxLength(8)  # 此处设置输入的最大长度为8
        line_text.move(0, 60)
        # line_text.setText()
        line_text.resize(260, 60)
        line_text.setStyleSheet("font-size:40px;")
        # line_text.setValidator(QIntValidator)

        def line_text1():
            lcd_number_class.setProperty("value", line_text.text())

        line_text.textChanged.connect(line_text1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
