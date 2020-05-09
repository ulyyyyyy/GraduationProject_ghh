from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from GUI.GraduationProUI import *
from GUI.his_alter import *
from read_history.read_history import read_history


class MyWindow(QMainWindow, Ui_GraduationPro):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_history.clicked.connect(self.get_his())

    def get_his(self):
        # 历史记录按钮功能
        read_history()

class History_Dialog(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    his_dialog = History_Dialog()

    btn_history = mywindow.btn_history
    btn_history.clicked.connect(his_dialog.show)

    mywindow.show()
    sys.exit(app.exec_())
