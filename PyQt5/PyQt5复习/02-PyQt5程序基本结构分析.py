# 导入依赖环境包
from cProfile import label
import sys
from PyQt5.Qt import *

# args = sys.argv
# print(args)  # 此处输出当前运行程序列表
# if args[0] == "1":
#     print("你好你好")
# else:
#     print("噢噢噢噢")

# 创建程序对象
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("这是一个程序标题")
window.resize(500, 200)
window.setStyleSheet("background-color:cyan;")

label = QLabel(window)
label.setText("这是一个label文本")
label.setStyleSheet("color:red;")

window.show()

sys.exit(app.exec_())
