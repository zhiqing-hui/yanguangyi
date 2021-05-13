# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_Form  ###导入UI

class menu_win(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)  # 父类的构造函数
        self.setupUi(self)
        self.slot_init()  # 初始化槽函数t自带的，会关闭程序




    def slot_init(self):
        self.pushButton_quguangdu.clicked.connect(self.display_quguangdu)
        self.pushButton_qulv.clicked.connect(self.display_qulv)
        self.pushButton_moshi.clicked.connect(self.display_moshi)
        self.pushButton_printset.clicked.connect(self.display_printset)
        self.pushButton_data.clicked.connect(self.display_data)
    def display_quguangdu(self):
        #设置当前可见的选项卡的索引
        self.stackedWidget.setCurrentIndex(0)
    def display_qulv(self):
        #设置当前可见的选项卡的索引
        self.stackedWidget.setCurrentIndex(1)
    def display_moshi(self):
        #设置当前可见的选项卡的索引
        self.stackedWidget.setCurrentIndex(2)
    def display_printset(self):
        #设置当前可见的选项卡的索引
        self.stackedWidget.setCurrentIndex(3)
    def display_data(self):
        #设置当前可见的选项卡的索引
        self.stackedWidget.setCurrentIndex(4)