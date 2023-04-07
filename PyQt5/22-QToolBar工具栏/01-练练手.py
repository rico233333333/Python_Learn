import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("工具栏")
        self.tool_bar()
        self.show()

    def tool_bar(self):
        # 菜单栏
        bar = QtWidgets.QMenuBar(self)
        bar.setGeometry(0,0,800,30)
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

        # 工具栏创建
        toolbar = QToolBar(self)
        toolbar.setGeometry(0,30,800,30)
        toolbar.setObjectName("toolbar")
        file = toolbar.addAction("多Excel文件夹处理")
        toolbar.addSeparator()
        toolbar.addAction("单一Excel")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
