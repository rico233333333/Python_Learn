import sys
from PyQt5.Qt import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("MID小窗口")
        self.mdi()
        self.show()

    def mdi(self):
        # 创建MDI区域
        mid = QMdiArea(self)
        mid.setObjectName("mdiArea")
        mid.setGeometry(0,30,1920,800)

        # 创建三个button
        but01 = QPushButton(self)
        but01.setText("添加子窗口")

        but02 = QPushButton(self)
        but02.setText("删除子窗口")

        but03 = QPushButton(self)
        but03.setText("平铺展示")

        but04 = QPushButton(self)
        but04.setText("级联展示")

        self.connt = 0  # 定义初始化页面个数

        # 按钮水平布局
        halout = QHBoxLayout(self)
        halout.addWidget(but01,QtCore.Qt.AlignTop)
        halout.addWidget(but02,QtCore.Qt.AlignTop)
        halout.addWidget(but03,QtCore.Qt.AlignTop)
        halout.addWidget(but04,QtCore.Qt.AlignTop)

        def but01_cao():  # 新建
            sub = QMdiSubWindow()  # 创建子窗口对象
            sub.setWindowTitle("子窗口"+str(self.connt))
            sub.resize(200,200)
            lab = QLabel(sub)
            lab.move(10,30)
            # lab.setStyleSheet()
            self.connt = self.connt + 1
            lab.setText("这是第"+str(self.connt)+"个子窗口")
            # 将子窗口添加到MDI区域
            mid.addSubWindow(sub)
            print(mid.subWindowList())
            sub.show()

        def but02_cao():  # 删除
            if len(mid.subWindowList()) == 0:
                print("请点击添加子窗口按钮")
            else:
                mid.removeSubWindow(mid.subWindowList()[0])

        def but03_cao():  # 平铺展示
            if len(mid.subWindowList()) == 0:
                print("平铺无效，请添加子窗口")
            else:
                mid.tileSubWindows()

        def but04_cao():  # 级联展示
            if len(mid.subWindowList()) == 0:
                print("级联无效，请添加子窗口")
            else:
                mid.cascadeSubWindows()

        but01.clicked.connect(but01_cao)
        but02.clicked.connect(but02_cao)
        but03.clicked.connect(but03_cao)
        but04.clicked.connect(but04_cao)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
