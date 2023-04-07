import sys

from PyQt5 import QtGui
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("这是一个窗口")
        self.resize(322,500)
        self.q_font_combo_box()
        self.show()

    def q_font_combo_box(self):
        q_f_c_b01 = QFontComboBox(self)
        q_f_c_b01.resize(222,40)
        q_f_c_b01.move(50,30)
        q_f_c_b01.setStyleSheet("font-size:20px")

        lab01 = QLabel(self)
        lab01.setText("每天编程一小时，以后秃头每一天")
        lab01.setStyleSheet('font-size:16px')
        lab01.move(50,100)
        
        def label_text():
            lab01.setFont(QtGui.QFont(q_f_c_b01.currentText()))

        q_f_c_b01.activated.connect(label_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
