import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("CommandLinkButton 命令链接按钮")
        self.resize(400,400)
        self.q_command_link_button()
        self.show()

    def q_command_link_button(self):
        q_command_link_button01 = QCommandLinkButton(self)
        q_command_link_button01.setText("https://www.baidu.com")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
