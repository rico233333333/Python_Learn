import sys
from PyQt5.Qt import *
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("这是一个窗口标题")
        self.grid()
        self.show()

    def grid(self):
        grid = QGridLayout(self)  # 创建网格布局
        # 创建文本标签
        label = QLabel(self)
        label.setText("用户名：")
        # 创建输入文本框
        line_input = QLineEdit(self)
        line_input.setPlaceholderText("请输入用户名")
        # 创建标签文本
        label_password = QLabel(self)
        label_password.setText("密码：")
        # 创建输入文本框
        line_password = QLineEdit(self)
        line_password.setPlaceholderText("请输入密码")
        line_password.setEchoMode(line_password.PasswordEchoOnEdit)
        # 创建登录按钮
        login_button = QPushButton(self)
        login_button.setText("登录")
        # 创建取消按钮
        cancel_button = QPushButton(self)
        cancel_button.setText("取消")
        grid.addWidget(label, 0, 0, QtCore.Qt.AlignLeft)  # 设置左对齐
        grid.addWidget(line_input, 0 , 1,QtCore.Qt.AlignLeft)  # 设置左对齐
        grid.addWidget(label_password,1,0,QtCore.Qt.AlignLeft)  # 设置左对齐
        grid.addWidget(line_password,1,1,QtCore.Qt.AlignLeft)
        grid.addWidget(login_button,2,0,QtCore.Qt.AlignCenter)
        grid.addWidget(cancel_button,2,1,QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
