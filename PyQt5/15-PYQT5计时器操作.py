# 导入库
import sys
from PyQt5.Qt import *


class MyObject(QObject):
    def startTimer(self, evt):
        return
# 创建一个应用程序主框架、
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("定时器的使用")
window.resize(500,500)  # 设置大小
obj = MyObject()
timer_id = obj.startTimer(1)  # 1000ms也就是1000毫秒 后面是精确程度 毫秒级准确
print(timer_id)
window.show()
sys.exit(app.exec_())