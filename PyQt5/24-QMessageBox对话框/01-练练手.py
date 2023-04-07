import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import QMessageBox


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("QMessageBox对话框")
        self.q_message_box()
        self.show()

    def q_message_box(self):
        # 创建消息按钮
        but01 = QPushButton(self)
        but01.setText("消息框")
        # 创建警告按钮
        but02 = QPushButton(self)
        but02.setText("警告框")
        # 创建问答框按钮
        but03 = QPushButton(self)
        but03.setText("问答框")
        # 创建错误按钮
        but04 = QPushButton(self)
        but04.setText("错误框")
        # 创建关于按钮
        but05 = QPushButton(self)
        but05.setText("关于框")

        # 创建水平布局
        q_hbox = QHBoxLayout(self)
        q_hbox.addWidget(but01)
        q_hbox.addWidget(but02)
        q_hbox.addWidget(but03)
        q_hbox.addWidget(but04)
        q_hbox.addWidget(but05)

        # 定义消息对话框
        def information():
            message = QMessageBox.information(None, "消息", "这是一个消息对话框", QMessageBox.Ok|QMessageBox.No)
            if QMessageBox.Ok == message:
                QMessageBox.information(self,"同意","您同意了本次请求")

        # 定义警告对话框
        def warn():
            QMessageBox.warning(None, "错误", "这是一个错误对话框", QMessageBox.Ok)

        # 定义问答对话框
        def question():
            QMessageBox.question(None, "问答", "这是一个问答对话框", QMessageBox.Ok)

        # 定义错误对话框
        def critical():
            QMessageBox.critical(None, "错误", "这是一个错误对话框", QMessageBox.Ok)

        # 定义关于对话框
        def about():
            QMessageBox.about(None, "关于", "这是一个关于对话框")

        # 链接槽函数
        but01.clicked.connect(information)
        but02.clicked.connect(warn)
        but03.clicked.connect(question)
        but04.clicked.connect(critical)
        but05.clicked.connect(about)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
