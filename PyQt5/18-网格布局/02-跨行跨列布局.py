import sys
from PyQt5.Qt import *
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("跨行跨列的网格布局")
        self.q_grid_Layout()
        self.show()

    def q_grid_Layout(self):
        q_grid_layout = QGridLayout(self)  # 调用QGridLayout类
        lab01 = QLabel(self)
        lab01.setText("用户名：")
        line_edit01 = QLineEdit(self)
        line_edit01.setPlaceholderText("请输入用户名")
        lab02 = QLabel(self)
        lab02.setText("密码：")
        line_edit02 = QLineEdit(self)
        line_edit02.setPlaceholderText("请输入密码")

        but01 = QPushButton(self)
        but01.setText("登录")

        q_grid_layout.addWidget(lab01,0,0,QtCore.Qt.AlignLeft)  # 用户名
        q_grid_layout.addWidget(line_edit01,0,1,QtCore.Qt.AlignLeft)

        q_grid_layout.addWidget(lab02,1,0,QtCore.Qt.AlignLeft)  # 密码
        q_grid_layout.addWidget(line_edit02,1,1,QtCore.Qt.AlignLeft)
        q_grid_layout.addWidget(but01,2,0,QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
