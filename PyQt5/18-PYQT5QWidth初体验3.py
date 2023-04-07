import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget初体验3")
        self.resize(600,500)
        self.move(300,400)
        self.setup()
        self.show()

    def setup(self):
        widget_count = 20
        column_count = 3  # 设置列数目
        # 计算一个控件的宽度
        widget_width = self.width()/column_count
        # 总共有多少行（编号//一行多少列 + 1）
        row_count = (widget_count - 1) // column_count + 1
        widget_height = self.height() / row_count

        for i in range(0, widget_count):
            w = QWidget(self)
            w.resize(widget_width , widget_height)
            widget_x = i % column_count * widget_width
            widget_y = i // column_count * widget_height
            w.move(widget_x,widget_y)
            w.setStyleSheet("background-color:black;border:1px solid yellow;")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())