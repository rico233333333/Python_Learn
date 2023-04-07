# -*- coding:gbk -*-

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("����һ������")
        self.resize(500, 400)
        self.textEdit()
        self.show()

    def textEdit(self):
        textEdit1 = QTextEdit(self)
        textEdit1.setPlainText('�ճ������������Ϣ��'
                               '�侮�����������ʳ��'
                               '�������Һ����գ�')
        print(textEdit1.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
