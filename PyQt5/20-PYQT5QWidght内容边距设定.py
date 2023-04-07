from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置内容边距")
        self.move(600, 400)
        self.resize(600, 800)
        self.setup()
        self.show()

    def setup(self):
        lab1 = QLabel(self)
        lab1.setText("社会我李哥，人狠话不多")
        lab1.setStyleSheet("background-color:skyblue;")
        lab1.resize(300, 300)
        lab1.setContentsMargins(100, 0, 0, 0)  # (左, 上, 右, 下)  # 设置边距
        a = lab1.getContentsMargins()  # 输出边距
        print(a, type(a))


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
