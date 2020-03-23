# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraduationProject.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraduationPro(object):
    def setupUi(self, GraduationPro):
        GraduationPro.setObjectName("GraduationPro")
        GraduationPro.resize(893, 582)
        self.centralwidget = QtWidgets.QWidget(GraduationPro)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1100, 750))
        self.tabWidget.setMinimumSize(QtCore.QSize(1100, 750))
        self.tabWidget.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.tabWidget.setStyleSheet("border-color: rgb(170, 170, 255);")
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.btn_analyse_all = QtWidgets.QPushButton(self.tab1)
        self.btn_analyse_all.setGeometry(QtCore.QRect(520, 340, 201, 91))
        self.btn_analyse_all.setObjectName("btn_analyse_all")
        self.btn_history = QtWidgets.QPushButton(self.tab1)
        self.btn_history.setGeometry(QtCore.QRect(180, 340, 201, 91))
        self.btn_history.setObjectName("btn_history")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.textEdit = QtWidgets.QTextEdit(self.tab2)
        self.textEdit.setGeometry(QtCore.QRect(60, 60, 631, 421))
        self.textEdit.setObjectName("textEdit")
        self.btn_analyse_singlt = QtWidgets.QPushButton(self.tab2)
        self.btn_analyse_singlt.setGeometry(QtCore.QRect(730, 400, 131, 81))
        self.btn_analyse_singlt.setObjectName("btn_analyse_singlt")
        self.tabWidget.addTab(self.tab2, "")
        GraduationPro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GraduationPro)
        self.statusbar.setObjectName("statusbar")
        GraduationPro.setStatusBar(self.statusbar)
        self.actionHow_to_use_this_Programming = QtWidgets.QAction(GraduationPro)
        self.actionHow_to_use_this_Programming.setObjectName("actionHow_to_use_this_Programming")

        self.retranslateUi(GraduationPro)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GraduationPro)

    def retranslateUi(self, GraduationPro):
        _translate = QtCore.QCoreApplication.translate
        GraduationPro.setWindowTitle(_translate("GraduationPro", "上网行为分析系统"))
        self.btn_analyse_all.setText(_translate("GraduationPro", "一键分析"))
        self.btn_history.setText(_translate("GraduationPro", "导出历史记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("GraduationPro", "一键分析"))
        self.btn_analyse_singlt.setText(_translate("GraduationPro", "单段文本分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("GraduationPro", "单个文本分析"))
        self.actionHow_to_use_this_Programming.setText(_translate("GraduationPro", "How to use this Programming"))
