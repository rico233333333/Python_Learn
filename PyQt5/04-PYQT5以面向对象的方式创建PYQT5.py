"""
@Project : Python爬虫
@File    : 04-PYQT5以面向对象的方式创建PYQT5.py
@Author  : Ricard.Cohen
@Date    : 2022/4/8 23:14
"""
# 导入依赖环境(包和模块)
from PyQt5.Qt import *  # 主要包含了一些常用的类 做了一个简单汇总
import sys  #

"""# sys.argv 当别人通过命令行启动这个程序的时候，可以设定一种功能（接受命令行传递的参数，来执行不同的业务逻辑）

# 第一步 创建一个应用程序对象
# 调用QApplication()类
# 并且传入了sys.srgv 命令行传参
app = QApplication(sys.argv)
#print(app.arguments())  # 获取变量
#print(qApp.arguments())  # 获取全局变量

# 第二步 创建主窗口
# 创建主窗口

window = QWidget() # 调用QWidget()类
# 设置控件
window.setWindowTitle("")  # 设置窗口title
window.resize(400,500)  # 设置窗口大小 400为宽500为高
window.move(300,200)  # 窗口定位 先左后上



# 展示控件
window.show()
# 第三步 进入事件循环
# 保证程序不会退出
# 检测交互信息
sys.exit(app.exec_())  # 事件循环


#sys.exit()
#退出程序正常退出返回0
#不正常退出返回1
#打断退出-1"""

# 面向对象编程


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

app = QApplication(sys.argv)
window = Wnidow()
sys.exit(app.exec_())