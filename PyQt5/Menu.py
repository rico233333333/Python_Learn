"""
@Project : Python爬虫
@File    : Menu.py
@Author  : Ricard.Cohen
@Date    : 2022/4/8 23:59
"""
from PyQt5.Qt import *  # 主要包含了一些常用的类 做了一个简单汇总

class Wnidow(QWidget):
    def __init__(self):  # 此处self是一个实例对象
        super().__init__()  # 此处对QWidget的init方法进行重写
        self.setWindowTitle("呜呜呜，这还是QT开发的程序")
        self.resize(300,300)
        self.setup_gui()  # 调用setup_gui方法
        self.show()  # 展示控件

    def setup_gui(self):
        lable = QLabel(self)
        lable.setText("我爱你呀憨批")
        lable.move(100,100)