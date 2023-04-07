from PyQt5.Qt import *
import sys
import random as rm

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("点击按钮，控制台输出文本")
        self.resize(300,200)  # 定义窗口大小 长300 高200
        self.Object对象信号操作()
        self.lab()
        self.windowWindow()
        self.show()

    def Object对象信号操作(self):
        # 定义点击次数
        X = 0
        but = QPushButton(self)  # 此处把QPushButton写入到窗口里边
        but.setText("点我试试看")
        def say(X):
            print("点我干嘛，憨批",lambda X : X)
        # 事件绑定
        but.clicked.connect(say)

    def lab(self):
        lab2 = QLabel(self)
        lab2.move(200, 30)
        def cao():
            a = rm.randint(1,10)
            a = str(a)
            lab2.setText(a)
            print(a)
        lab1 = QLabel(self)
        lab1.setText("猜数字，生成的数字是：")
        lab1.move(0,30)
        but2 = QPushButton(self)
        but2.setText("点击生成随机数")
        but2.move(0,100)
        but2.clicked.connect(cao)

    def windowWindow(self):
        # 定义新窗口
        win = QWidget(self)
        def cao(title):
            print("改变了，窗口标题",title)
        win.windowTitleChanged.connect(cao)
        win.setWindowTitle("ohhhh")
        win.setWindowTitle("ooooo")


app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("ohhhh")
win.resize(1000,300)
def cao(title):
    print("改变了，窗口标题",title)
    # win.windowTitleChanged.disconnect()  # 取消事件绑定
    win.blockSignals(True)  # 暂停信号传输
    win.setWindowTitle("聊天呀-"+title)
    # win.windowTitleChanged.connect(cao)  # 重新绑定事件
    win.blockSignals(False)  # 恢复事件连接
win.windowTitleChanged.connect(cao)
win.setWindowTitle("ohhhh")
win.setWindowTitle("ooooo1")
win.setWindowTitle("ooooo2")
win.setWindowTitle("ooooo3")
win.setWindowTitle("ooooo4")
win.setWindowTitle("ooooo5")
win.show()
window = Window()
sys.exit(app.exec_())