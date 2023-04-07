import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("文件对话框")
        self.file_dialog()
        self.show()

    def file_dialog(self):
        # 创建按钮控件
        but_choice = QPushButton(self)
        but_choice.setText("选择文件")
        # 删除文件
        but_clear = QPushButton(self)
        but_clear.setText("删除文件")

        # 创建列表控件
        list_widget = QListWidget(self)
        list_widget.setViewMode(list_widget.IconMode)

        # 创建文件对话框函数
        def q_file_dialog_cao():
            q_file_dialog = QFileDialog(self)
            q_file_dialog.setFileMode(q_file_dialog.ExistingFiles)  # 设置多选
            q_file_dialog.setDirectory("C:\\")  # 设置默认盘为C盘
            # 设置文件格式
            q_file_dialog.setNameFilter("图片文件(*.jpg *.png *.ico)")
            if q_file_dialog.exec_():
                list_widget.addItems(q_file_dialog.selectedFiles())  # 将文件显示在列表中

            # print(list_widget.text())

        # 创建删除文件选择函数
        def clear_list_file():
            message_information = QMessageBox(self)
            # if list_widget.


        # 链接槽函数
        but_choice.clicked.connect(q_file_dialog_cao)

        # 创建垂直布局
        q_h_box = QVBoxLayout(self)
        q_h_box.addWidget(but_choice)
        q_h_box.addWidget(but_clear)
        q_h_box.addWidget(list_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
