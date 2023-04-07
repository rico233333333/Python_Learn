from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)

window1 = QWidget()
window1.setWindowTitle("窗口1")
window1.resize(600,800)
window1.setStyleSheet("background-color:cyan;")


window2 = QWidget()
window2.resize(300,200)
window2.setStyleSheet("background-color:skyblue;")

window1.show()
window2.setParent(window1)
window2.show()



sys.exit(app.exec_())
