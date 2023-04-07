"""
@Poject : Python爬虫
@File   : test.py
@Author : Ricard.Cohe
@Date   : 2022/4/8 10:42
"""
from PyQt5.Qt import *
import sys

# 创建主类，内藏玄机
class Window(QWidget):
    def __init__(self):  # 此处self相当于window 是一个实例属性
        super().__init__()
        self.setWindowTitle("此处设置窗口标题")
        self.resize(300,300)  #此处设置窗口大小，分别是宽高
        self.创建的类方法()
        self.show()  # 把所有组件都加入布局

    def 创建的类方法(self):
        # 此处填写对应的组件
        pass

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())