# 导入对应的库
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("类型判定")
        self.resize(500, 600)
        self.QObject类型判定()
        self.show()

    def QObject类型判定(self):
        '''obj = QObject()
        w = QWidget()
        btn = QPushButton()
        lab = QLabel()
        lst = [obj, w, btn, lab]
        for i in lst:
            print("1111", i.isWidgetType())  # 此处判断对象是否是控件 是True 否False
            print("2222", i.inherits("QObject"))  # 判断是否继承自父类'''
        # 判定标签改变标签颜色
        # 创建三个标签 分别是QLabel QLabel QPushButton
        Qlab1 = QLabel(self)
        Qlab1.setText("你猜你猜")
        Qlab2 = QLabel(self)
        Qlab2.setText("我猜不到啊，傻逼")
        Qlab2.move(100,100)
        QPB = QPushButton(self)
        QPB.setText("点我试试看")
        QPB.move(200,200)
        # 筛选对应的控件
        lst = [Qlab1,Qlab2,QPB]
        for i in lst:
            if i.inherits("QLabel") == True:
                i.setStyleSheet("background-color:yellow;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
