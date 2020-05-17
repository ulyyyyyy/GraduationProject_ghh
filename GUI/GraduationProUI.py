# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraduationProject.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import test_qrc


class Ui_GraduationPro(object):
    def setupUi(self, GraduationPro):
        GraduationPro.setObjectName("GraduationPro")
        GraduationPro.resize(1012, 653)
        self.centralwidget = QtWidgets.QWidget(GraduationPro)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 40, 941, 581))
        self.graphicsView.setStyleSheet("border-image: url(:/newPrefix/desktop.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 90, 561, 141))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.btn_history = QtWidgets.QPushButton(self.centralwidget)
        self.btn_history.setGeometry(QtCore.QRect(290, 260, 171, 71))
        self.btn_history.setObjectName("btn_history")
        self.btn_analyse_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analyse_all.setGeometry(QtCore.QRect(560, 260, 171, 71))
        self.btn_analyse_all.setObjectName("btn_analyse_all")
        GraduationPro.setCentralWidget(self.centralwidget)
        self.actionHow_to_use_this_Programming = QtWidgets.QAction(GraduationPro)
        self.actionHow_to_use_this_Programming.setObjectName("actionHow_to_use_this_Programming")

        self.retranslateUi(GraduationPro)
        QtCore.QMetaObject.connectSlotsByName(GraduationPro)

    def retranslateUi(self, GraduationPro):
        _translate = QtCore.QCoreApplication.translate
        GraduationPro.setWindowTitle(_translate("GraduationPro", "上网行为分析系统"))
        self.label.setText(_translate("GraduationPro", "上网行为分析系统"))
        self.btn_history.setText(_translate("GraduationPro", "导出历史记录"))
        self.btn_analyse_all.setText(_translate("GraduationPro", "一键分析"))
        self.actionHow_to_use_this_Programming.setText(_translate("GraduationPro", "How to use this Programming"))
