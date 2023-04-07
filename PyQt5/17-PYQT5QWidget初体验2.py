import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget初体验2")
        self.move(300,200)  # 此处包含窗口框架的定位 第一个代表x,第二个代表y
        self.resize(500,600)  # 设置用户可操作区域的大小 第一个表示宽，第二个表示高
        self.setupGui()
        self.show()

    def setupGui(self):
        lambda1 = QLabel(self)
        lambda1.setText("这是一个lambda文本标签")
        # 设置lambda文本标签的样式
        lambda1.setStyleSheet("background-color:skyblue;font-size:24px;")
        lambda1.move(0,300)
        def btn():
            text = lambda1.text()
            a = text+"这是一个lambda文本标签"
            lambda1.setText(a)
            lambda1.adjustSize()
            print(a)
        btn1 = QPushButton(self)
        btn1.setText("点我试试看")
        btn1.clicked.connect(btn)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
