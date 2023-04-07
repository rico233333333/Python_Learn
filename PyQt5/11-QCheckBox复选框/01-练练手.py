import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QMessageBox

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("CheckBox 复选框")
        self.q_check_box()
        self.show()

    def q_check_box(self):
        q_check_box01 = QCheckBox(self)
        q_check_box01.setText("基本信息管理")
        q_check_box01.move(20,20)

        q_check_box02 = QCheckBox(self)
        q_check_box02.setText("权限管理")
        q_check_box02.move(150,20)

        q_push_button = QPushButton(self)
        q_push_button.setText("设置权限")
        q_push_button.move(20,80)

        def q_check_box():
            over  = ""
            if q_check_box01.isChecked():
                over = over+q_check_box01.text()
            if q_check_box02.isChecked():
                over = over+'\n'+q_check_box02.text()
            print(over)
            QMessageBox.information(self,"提示","您选择的权限如下：\n"+over,QMessageBox.Ok)
        q_push_button.clicked.connect(q_check_box)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
