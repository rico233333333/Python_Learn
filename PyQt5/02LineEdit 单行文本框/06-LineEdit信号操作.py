import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置窗口标题")
        self.resize(400, 300)
        self.LineEdit()
        self.show()

    def LineEdit(self):
        def shou():
            print("输入的内容改变了")

        def shuo_1():
            print("文本框内容编辑结束")
        lineEdit = QLineEdit(self)
        lineEdit.textChanged.connect(shou)

        lineEdit_1 = QLineEdit(self)
        lineEdit_1.setFocus(True)
        lineEdit_1.editingFinished.connect(shuo_1)
        lineEdit_1.move(0, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
