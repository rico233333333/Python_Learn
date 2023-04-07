import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap  # 导入图片类


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("登录")
        self.resize(535, 410)
        self.setMaximumSize(535, 410)
        self.setMinimumSize(535, 410)
        self.login()
        self.show()

    def login(self):
        # 放置图片
        label = QLabel(self)
        label.setPixmap(QPixmap(r"./jpg/img.png"))
        label.resize(535, 155)
        label.setScaledContents(True)

        # 设置欢迎文字
        label_welcome = QLabel(self)
        label_welcome.setText("欢迎你尊敬的：普通用户")
        label_welcome.resize(535, 155)
        label_welcome.setStyleSheet("font-size:40px;color:white;")
        label_welcome.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        # 账号模块
        label_login = QLabel(self)
        label_login.move(120, 205)
        label_login.setText("账号：")
        label_login.setStyleSheet("font-size:25px")

        line_Edit_login = QLineEdit(self)
        line_Edit_login.move(180, 200)
        line_Edit_login.resize(239, 30)
        line_Edit_login.setStyleSheet("font-size:25px")
        line_Edit_login.setPlaceholderText("请输入登录账号")

        label_password = QLabel(self)
        label_password.move(120, 255)
        label_password.setStyleSheet("font-size:25px")
        label_password.setText("密码：")

        line_Edit_password = QLineEdit(self)
        line_Edit_password.move(180, 255)
        line_Edit_password.resize(239, 30)
        line_Edit_password.setStyleSheet("font-size:25px")
        line_Edit_password.setPlaceholderText("请输入登录密码")
        line_Edit_password.setEchoMode(line_Edit_password.PasswordEchoOnEdit)

        # 登录模块选择-普通用户
        q_radio_button = QRadioButton(self)
        q_radio_button.setText("普通用户")
        q_radio_button.setChecked(True)
        q_radio_button.move(120, 300)
        q_radio_button.setStyleSheet("font-size:20px")

        # 登录模块选择-管理用户
        q_radio_button_g = QRadioButton(self)
        q_radio_button_g.setText("管理用户")
        q_radio_button_g.setChecked(False)
        q_radio_button_g.move(320, 300)
        q_radio_button_g.setStyleSheet("font-size:20px")

        q_push_button_login = QPushButton(self)
        q_push_button_login.resize(300, 45)
        q_push_button_login.setText("登录")  # 设置文字
        q_push_button_login.move(120, 340)
        q_push_button_login.setStyleSheet("font-size:25px;background-color:DeepSkyBlue;")  # 设置字体大小
        q_push_button_login.setIcon(QtGui.QIcon("./jpg/login.png"))  # 图标路径
        q_push_button_login.setIconSize(QtCore.QSize(25, 25))  # 设置图标大小

        # 定义槽函数
        login = "3439758907"
        password = "Like20020412"

        def push_button_login():
            if line_Edit_login.text() == login and line_Edit_password.text() == password:
                if q_radio_button.isChecked() == True:
                    label_welcome.setText("欢迎你尊敬的：" + q_radio_button.text())
                    print("登录成功，欢迎你 " + q_radio_button.text(), line_Edit_login.text())
                else:
                    label_welcome.setText("欢迎你尊敬的：" + q_radio_button_g.text())
                    print("登录成功，欢迎你 " + q_radio_button_g.text(), line_Edit_login.text())
            else:
                print("账号密码错误，登录失败,请重新输入！！！")

        q_push_button_login.clicked.connect(push_button_login)

        # 设置Label文本切换
        def radio_change():
            if q_radio_button.isChecked() == True:
                label_welcome.setText("欢迎你尊敬的：" + q_radio_button.text())
            else:
                label_welcome.setText("欢迎你尊敬的：" + q_radio_button_g.text())

        q_radio_button.toggled.connect(radio_change)

        q_radio_button_g.toggled.connect(radio_change)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
