from PyQt5.Qt import *
import sys

# 调用QApplication()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建窗口
    # 创建窗口(父窗口)
    w1 = QWidget()
    w1.setWindowTitle("父窗口")  # 设置父窗口标题
    w1.resize(600, 800)
    but = QPushButton()
    but.setParent(w1)
    but.setText("点我试试看")
    but.move(0, 780)
    w1.show()
    print(type(w1))
    # 创建窗口(子窗口)
    w2 = QWidget()
    w2.setStyleSheet("background-color:white")
    w2.resize(600, 780)
    w2.setParent(w1)
    but = QPushButton()
    but.setParent(w2)
    but.setText("点我试试看")
    but.move(0, 760)

    # 创建label标签文本
    lab01 = QLabel()
    lab01.setText("label01")
    lab01.setParent(w2)
    # 继续创建Label文本
    lab02 = QLabel()
    lab02.setText("Label02")
    lab02.setParent(w2)
    lab02.move(100, 100)

    # 创建样式
    # 动态获取标签，动态赋予其样式
    for i in w2.findChildren(QLabel):
        i.setStyleSheet("background-color:yellow;")
    w2.show()
    sys.exit(app.exec_())
