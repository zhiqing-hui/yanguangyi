# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev_win.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 581, 411))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_Z_UP = QtWidgets.QPushButton(self.page)
        self.pushButton_Z_UP.setGeometry(QtCore.QRect(60, 110, 101, 41))
        self.pushButton_Z_UP.setObjectName("pushButton_Z_UP")
        self.pushButton_Z_DOWN = QtWidgets.QPushButton(self.page)
        self.pushButton_Z_DOWN.setGeometry(QtCore.QRect(60, 230, 101, 41))
        self.pushButton_Z_DOWN.setObjectName("pushButton_Z_DOWN")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Z_UP.setText(_translate("MainWindow", "Z轴电机向上"))
        self.pushButton_Z_DOWN.setText(_translate("MainWindow", "Z轴电机向下"))

