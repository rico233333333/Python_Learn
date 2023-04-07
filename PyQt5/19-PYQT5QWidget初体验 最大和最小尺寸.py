from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("最大和最小尺寸")
        self.move(200,300)  # x\y
        self.setMaximumSize(400,800)
        self.setMinimumSize(300,500)
        self.setup()
        self.show()

    def setup(self):
        W = QWidget(self)
        W.setStyleSheet("background-color:skyblue;")


app = QApplication(sys.argv)
window = Window()
print(window.size())
sys.exit(app.exec_())
