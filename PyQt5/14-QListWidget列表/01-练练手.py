import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget列表控件")
        self.resize(1000, 500)
        self.q_list_widget()
        self.show()

    def q_list_widget(self):
        list = ["1", "2"]
        q_list_widget = QListWidget(self)
        q_list_widget.addItems(list)
        q_list_widget.item(1).setToolTip("点一下这个")
        q_list_widget.item(0).setToolTip("没有功能")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
