import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("设置窗口标题")
        self.resize(500, 400)
        self.textEdit()
        self.show()

    def textEdit(self):
        textEdit = QTextEdit(self)
        textEdit.setPlainText('日出而作，日入而息。'
                              '凿井而饮，耕田而食。'
                              '帝力于我何有哉！')
        textEdit.wordWrapMode()  # 设置自动换行


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
