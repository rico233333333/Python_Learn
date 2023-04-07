import sys
from PyQt5.Qt import *


# 以面向对象的手法写出来
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget初体验")
        self.move(300,300)  # 设置窗口的绝对坐标
        self.resize(500,500)  # 设置操作区域的大小
        self.show()


app = QApplication(sys.argv)
window = Window()
print(window.x())  # 获取左上顶点距离窗口或者桌面的值
print(window.y())  # 获取左上角顶点距离窗口
print(window.pos())  # 获取x()、y()函数的值做一个汇总
print(window.width())  # 获取用户可操作性区域的宽
print(window.height())  # 获取用户可操作区域的高
print(window.size())  # 获取用户可操作性区域的具体信息
print(window.geometry())  # 获取用户区域相对于父控件的位置和尺寸组合
print(window.rect())  # 获取 x , y ,width ,height的组合
print(window.frameSize())  # 获取框架大小
print(window.frameGeometry())
sys.exit(app.exec_())
