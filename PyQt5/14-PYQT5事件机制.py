# 导入对应的库
import sys
from PyQt5.Qt import *


class App(QApplication):
    def notify(self,QObject,QEvent):
        return super().notify(QObject,QEvent)