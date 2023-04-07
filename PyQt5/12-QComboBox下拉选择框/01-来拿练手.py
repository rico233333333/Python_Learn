import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("QComboxBox下拉按钮")
        self.resize(500, 500)
        self.q_combo_box()
        self.show()

    def q_combo_box(self):
        label01 = QLabel(self)
        label01.setText("职位:")
        label01.setStyleSheet("font-size:25px")
        label01.move(50, 33)

        list1 = ["总经理", "总监", "策划", "职员"]
        q_combo_box01 = QComboBox(self)
        q_combo_box01.addItems(list1)
        q_combo_box01.resize(200, 30)
        q_combo_box01.move(120, 30)
        q_combo_box01.setStyleSheet("font-size:25px")

        label02 = QLabel(self)
        label02.setText("您的选择为:" + q_combo_box01.currentText())
        label02.setStyleSheet("font-size:25px")
        label02.resize(400, 30)
        label02.move(50, 80)

        def cao_label():
            label02.setText("您的选择为:" + q_combo_box01.currentText())  # 获取选项中的文本

        q_combo_box01.activated.connect(cao_label)

        label03 = QLabel(self)
        label03.setText("输入需要新增添的文本")
        label03.setStyleSheet("font-size:25px")
        label03.move(50, 130)

        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText("请输入需要增添的文本")
        line_edit.setStyleSheet("font-size:25px")
        line_edit.setMaxLength(15)
        line_edit.resize(270, 26)
        line_edit.move(50, 180)

        label04 = QLabel(self)
        label04.setText("将设置或删除：\n'" + line_edit.text() + "'\n为新选项")
        label04.setStyleSheet("font-size:25px")
        label04.resize(400, 80)
        label04.setWordWrap(True)
        label04.move(50, 235)

        def line_text_change():
            label04.setText("将设置或删除：\n'" + line_edit.text() + "'\n为新选项")

        line_edit.textChanged.connect(line_text_change)

        but01 = QPushButton(self)
        but01.setText("增加一个")
        but01.setStyleSheet("font-size:25px")
        but01.move(50, 335)

        but02 = QPushButton(self)
        but02.setText("删除所有")
        but02.setStyleSheet("font-size:25px")
        but02.move(210, 335)

        def add():
            if line_edit.text() == '':
                print("请输入内容")
            else:
                q_combo_box01.addItem(line_edit.text())

        def clear():
            q_combo_box01.clear()
            label02.setText("当前无选择")

        but01.clicked.connect(add)
        but02.clicked.connect(clear)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
