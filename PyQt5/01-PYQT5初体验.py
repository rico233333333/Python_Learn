"""
@Poject : Python爬虫
@File   : 01-PYQT5初体验.py
@Author : Ricard.Cohe
@Date   : 2022/4/7 21:17
"""

from PyQt5.Qt import *
import sys

# app = QApplication(sys.argv)
app = QApplication(sys.argv)

window = QWidget()  # 调用主类
window.setWindowTitle("块点，秒男")  # 创建窗口
window.resize(400, 400)  # 设置窗口大小
window.move(400, 200)  # 顶部间距 ， 左侧间距

label = QLabel(window)  # 导入Label
label.setText("你喜欢谁")  # 设置Lable文本
label.move(200, 200)  # 设置label文本的位置 左，上
window.show()  # 关闭窗口
sys.exit(app.exec_())  # 执行程序，进入消息循环
