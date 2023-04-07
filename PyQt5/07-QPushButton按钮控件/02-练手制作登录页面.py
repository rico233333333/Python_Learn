import sys
from PyQt5.Qt import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
# import


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("登录")
        self.resize(535, 410)
        self.setMaximumSize(535,410)
        self.setMinimumSize(535,410)
        self.setStyleSheet("background-color:white;")
        self.login()
        self.show()

    def login(self):
        # 上方图片
        label = QLabel(self)
        label.resize(535, 155)
        label.setStyleSheet("background-color:cyan")
        # label.setStyleSheet("border-image:./png/background.jpg")
        label.setPixmap(QPixmap(r'./png/background.jpg'))
        # 账号模块
        label_login = QLabel(self)
        label_login.move(120, 205)
        label_login.setText("账号：")
        label_login.setStyleSheet("font-size:25px")

        line_Edit_login = QLineEdit(self)
        line_Edit_login.move(180,200)
        line_Edit_login.resize(239,30)
        line_Edit_login.setStyleSheet("font-size:25px")
        line_Edit_login.setPlaceholderText("请输入登录账号")


        label_password = QLabel(self)
        label_password.move(120, 255)
        label_password.setStyleSheet("font-size:25px")
        label_password.setText("密码：")

        line_Edit_password = QLineEdit(self)
        line_Edit_password.move(180,255)
        line_Edit_password.resize(239,30)
        line_Edit_password.setStyleSheet("font-size:25px")
        line_Edit_password.setPlaceholderText("请输入登录密码")

        q_push_button_login = QPushButton(self)
        q_push_button_login.resize(300, 45)
        q_push_button_login.setText("登录")  # 设置文字
        q_push_button_login.move(120, 340)
        q_push_button_login.setStyleSheet("font-size:25px;background-color:DeepSkyBlue;")  # 设置字体大小
        q_push_button_login.setIcon(QtGui.QIcon("./png/login.png"))  # 图标路径
        q_push_button_login.setIconSize(QtCore.QSize(25, 25))  # 设置图标大小

        # 定义槽函数
        login = "3439758907"
        password = "Like20020412"

        def push_button_login():
            if line_Edit_login.text() == login and line_Edit_password.text()==password:
                print("登录成功，欢迎你 ",line_Edit_login.text())
                self.window()
            else:
                print("账号密码错误，登录失败,请重新输入！！！")

        q_push_button_login.clicked.connect(push_button_login)

    def widget1(self):
        widget = QWidget(self)
        widget.resize(500,500)
        widget.setStyleSheet("background-color:cyan;")
        widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
