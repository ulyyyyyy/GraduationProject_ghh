from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QTableWidgetItem
import sys, os, re
from GUI.GraduationProUI import *
from GUI.his_alter import *
from GUI.check_file_exits import *
from read_history.read_history import read_history
from Clustering_Algorithm.k_means_2 import KmeansClustering
from data_cleaning.Extractor import Extractor

class MyWindow(QMainWindow, Ui_GraduationPro):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.path = r'C:\Users\叫乌鸦的少年怪\Desktop\历史记录文件.txt'
        self.btn_history.clicked.connect(lambda: self.get_his())
        self.btn_analyse_all.clicked.connect(lambda: self.show_analyse())
        self.btn_show_his_content.clicked.connect(lambda: self.set_table_content())
        self.file_exits_dialog = check_file_exits_Dialog()
        self.btn_search_web.clicked.connect(lambda: self.search_web_content())

    def get_his(self):
        # 历史记录按钮功能
        read_history()

    def show_analyse(self):
        a = KmeansClustering()
        a.keams_predict(r'C:\Users\叫乌鸦的少年怪\Desktop\content.txt')

    def set_table_content(self):
        if os.path.exists(self.path):
            with open(self  .path, 'r', encoding='utf-8') as txt:
                data = txt.readlines()
                self.table_row = len(data) - 1
                self.tableWidget.setColumnCount(1)
                self.tableWidget.setRowCount(self.table_row)
                for i in range(len(data)):
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(data[i]))
        else:
            self.file_exits_dialog.show()

    def search_web_content(self):
        url = self.lineEdit.text()
        print(url)
        ex = Extractor(threshold=30)
        html = ex.getHtml(url)
        content = ex.filter_tags(html)
        rlt = re.sub("\n", "", content)
        print(rlt)
        self.textEdit.setText(rlt)

class History_Dialog(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.close)


class check_file_exits_Dialog(QMainWindow, Check_file_exits_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()

    his_dialog = History_Dialog()
    btn_history = mywindow.btn_history
    btn_history.clicked.connect(his_dialog.show)

    mywindow.show()
    sys.exit(app.exec_())
