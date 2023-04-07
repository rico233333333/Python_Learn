"""
@Poject : Python爬虫
@File   : 02-PYQT5程序基本结构分析.py
@Author : Ricard.Cohe
@Date   : 2022/4/8 9:12
"""


# 导入依赖环境(包和模块)
from PyQt5.Qt import *  # 主要包含了一些常用的类 做了一个简单汇总
import sys  #


# sys.argv 当别人通过命令行启动这个程序的时候，可以设定一种功能（接受命令行传递的参数，来执行不同的业务逻辑）

'''args = sys.argv
print(args)
if args[0] == '1':
    print("helolo")
else :
    print("oooo")'''

# 第一步 创建一个应用程序对象
# 调用QApplication()类
# 并且传入了sys.srgv 命令行传参
app = QApplication(sys.argv)
# print(app.arguments())  # 获取变量
# print(qApp.arguments())  # 获取全局变量

# 第二步 创建主窗口
# 创建主窗口

window = QWidget()  # 调用QWidget()类
# 设置控件
window.setWindowTitle("赚钱，赚钱")  # 设置窗口title
window.resize(400, 500)  # 设置窗口大小 400为宽500为高
window.move(300, 200)  # 窗口定位 先左后上
# window.
label = QLabel(window)  # 此处需要传入主窗口
label.setText("我爱死你了")
label.move(200, 250)  # 设置label文本的位置
button = QPushButton(window)
button.move(0, 0)
button.setText("点击出现我爱你")
# 展示控件
window.show()
# 第三步 进入事件循环
# 保证程序不会退出
# 检测交互信息
sys.exit(app.exec_())  # 事件循环


# sys.exit()
# 退出程序正常退出返回0
# 不正常退出返回1
# 打断退出-1
