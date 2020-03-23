from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from GUI.GraduationProUI import *


class MyWindow(QMainWindow, Ui_GraduationPro):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
