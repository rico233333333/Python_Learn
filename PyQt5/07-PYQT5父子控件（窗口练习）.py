# 导入必要第三方库
import PyQt5.Qt
import sys

if __name__ == '__main__':
    app = PyQt5.Qt.QApplication(sys.argv)

    # 创建第一个窗口
    w1 = PyQt5.Qt.QWidget()
    w1.setStyleSheet("background-color:red;")
    w1.setWindowTitle("父窗口")
    w1.resize(800, 400)  # 设置窗口大小
    w1.move(300, 100)  # 设置窗口位置 距离左端300px 距离上端100px
    w1.show()  # 把w1 写入布局

    # 创建第二个窗口
    w2 = PyQt5.Qt.QWidget()
    w2.setStyleSheet("background-color:green;")
    w2.setWindowTitle("子窗口")
    w2.resize(400, 200)  # 设置子窗口大小
    """
    子窗口大小不会超过父窗口若是超过也仅仅是覆盖
    """

    # 创建父子对象关系
    w2.setParent(w1)

    w2.show()  # 把w2写入布局

    sys.exit(app.exec_())
