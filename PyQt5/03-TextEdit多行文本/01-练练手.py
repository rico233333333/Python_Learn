import io
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("??????????")
        self.resize(400, 300)
        self.textEdit()
        self.show()

    def textEdit(self):
        textEdit_1 = QTextEdit(self)
        textEdit_1.setPlainText('????????????????¦Æ???????????????'
                          '???????'
                          )  # ???????????

        print(textEdit_1.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
