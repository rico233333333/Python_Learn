import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("布局嵌套")
        self.q_form_layout()
        self.show()

    def q_form_layout(self):
        user = "理理理李先生"
        password = "1234567"

        q_form_layout = QFormLayout(self)  # 表单布局
        q_v_box_layout = QVBoxLayout(self)  # 垂直布局
        lab01 = QLabel(self)
        lab01.setText("用户名：")
        line_edit01 = QLineEdit(self)
        line_edit01.setPlaceholderText("请输入用户名")

        lab02 = QLabel(self)
        lab02.setText("密码：")
        line_edit02 = QLineEdit(self)
        line_edit02.setPlaceholderText("请输入密码")
        lab03 = QLabel(self)

        q_v_box_layout.addWidget(line_edit02)


        but01 = QPushButton(self)
        but01.setText("登录")

        but02 = QPushButton(self)
        but02.setText("取消")

        def but01_cao():
            if user == line_edit01.text() and password == line_edit02.text():
                print("登录成功")
            else :
                lab03.setText("密码错误，请重新输入")
                q_v_box_layout.addWidget(lab03)

        q_form_layout.addRow(lab01,line_edit01)
        q_form_layout.addRow(lab02,q_v_box_layout)
        q_form_layout.addRow(but01,but02)

        but01.clicked.connect(but01_cao)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
