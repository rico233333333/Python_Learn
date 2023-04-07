import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolButton 工具按钮")
        self.resize(500,600)
        self.q_tool_button()
        self.show()

    def q_tool_button(self):
        q_t_b = QToolButton(self)
        q_t_b.setText("测试")
        q_t_b.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        q_t_b.setArrowType(Qt.UpArrow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
