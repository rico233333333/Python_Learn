import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("QTabWidget选项卡")
        self.resize(500,500)
        self.q_tab_widget()
        self.show()

    def q_tab_widget(self):
        wid01 = QWidget(self)
        wid01.resize(400,400)
        wid01.setStyleSheet("background-color:cyan")

        wid02 = QWidget(self)
        wid02.resize(400,400)

        q_tab_widget = QTabWidget(self)
        q_tab_widget.addTab(wid01,"1号选项卡")
        q_tab_widget.addTab(wid02,"2号选项卡")
        q_tab_widget.resize(500,500)
        q_tab_widget.setTabsClosable(True)

        q_tab_widget.setCurrentWidget(wid01)
        # q_tab_widget.setCurrentWidget(wid02)
        # q_tab_widget.setCurrentWidget(wid02)
        print(q_tab_widget.currentIndex())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
