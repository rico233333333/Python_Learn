import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("表单布局")
        self.q_form_layout()
        self.show()

    def q_form_layout(self):
        q_form_layout = QFormLayout(self)  # 表单布局
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

        q_form_layout.addRow(lab01,line_edit01)
        q_form_layout.addRow(lab02,line_edit02)
        q_form_layout.addRow(but01)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
