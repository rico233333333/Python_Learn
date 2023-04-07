import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("QGroupBox分组框")
        self.resize(500,500)
        self.q_group_box()
        self.show()

    def q_group_box(self):
        q_group_box01 = QGroupBox(self)
        q_group_box01.setTitle("分组框1")
        q_group_box01.resize(250,500)
        q_group_box01.setFlat(True)
        q_group_box02 = QGroupBox(self)
        q_group_box02.setTitle("风组框2")
        q_group_box02.resize(250,500)
        q_group_box02.move(250,0)
        label = QLabel(self)
        label.setText("这是一个Label")
        label.setParent(q_group_box01)
        label.move(10,10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
