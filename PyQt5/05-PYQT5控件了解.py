"""
@Project : Python爬虫
@File    : 05-PYQT5控件了解.py
@Author  : Ricard.Cohen
@Date    : 2022/4/9 23:09
"""
from PyQt5.Qt import *
import sys

# 创建主类，内藏玄机
class Window(QWidget):
    def __init__(self):  # 此处self相当于window 是一个实例属性
        super().__init__()
        self.setWindowTitle("QSS样式应用")  # 此处设置标题
        self.resize(300,300)  #此处设置窗口大小，分别是宽高
        self.label()
        self.show()  # 把所有组件都加入布局

    def label(self):
        with open("QSS/05-PYQT控件了解.qss", "r") as f :
            qApp.setStyleSheet(f.read())
        label1 = QLabel(self)

        label1.setText("警告")
        print(label1.text())
        label1.setObjectName("notice")
        #print(label1.ObjectName())
        label1.setProperty("notice_worning","worning")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
# 此处脚本有误