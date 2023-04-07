import sys
from PyQt5.Qt import *
from PyQt5 import QtWidgets


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("菜单窗口")
        self.menu()
        self.show()

    def menu(self):
        bar = QtWidgets.QMenuBar(self)
        bar.setGeometry(40,0,700,30)
        file = bar.addMenu("文件")
        file.addAction("新建")
        file.addAction("打开")
        file.addAction("关闭")
        save = QAction("保存",self)  # 动作菜单
        save.setShortcut("Ctrl + S")
        file.addAction(save)
        quit = file.addMenu("Edit")  # 主菜单
        quit.addAction("Exit")  # 二级菜单

        tool = bar.addMenu("工具")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
