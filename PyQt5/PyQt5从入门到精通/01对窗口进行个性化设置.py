from PyQt5.Qt import *

import sys


class Window(QWidget):
    def __init__(self,x,y,lambda_txt):
        super().__init__()
        self.setWindowTitle(lambda_txt)
        self.resize(x, y)
        self.show()




app = QApplication(sys.argv)
window1 = Window(400,200,"这是一个标题")
window2 = Window(200,100,"标题2")
sys.exit(app.exec_())
