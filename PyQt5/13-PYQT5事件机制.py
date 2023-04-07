import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()  # 类的调用
btn = QPushButton(window)  # 继承
btn.setText("有种点一下")
btn.move(100,100)
def cao():
    print("你点击了按钮")
# 调用事件与槽
btn.pressed.connect(cao)
window.show()
sys.exit(app.exec_())