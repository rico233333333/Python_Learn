# -*- coding:gbk -*-

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("这是一个窗口")
        self.resize(500, 400)
        self.textEdit()
        self.show()

    def textEdit(self):
        textEdit1 = QTextEdit(self)
        textEdit1.setPlainText('日出而作，日入而息。'
                               '凿井而饮，耕田而食。'
                               '帝力于我何有哉！')
        print(textEdit1.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
