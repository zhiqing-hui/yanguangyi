# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 755)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_opencamer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_opencamer.setGeometry(QtCore.QRect(274, 80, 101, 23))
        self.pushButton_opencamer.setObjectName("pushButton_opencamer")
        self.pushButton_caculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_caculate.setGeometry(QtCore.QRect(940, 180, 75, 23))
        self.pushButton_caculate.setObjectName("pushButton_caculate")
        self.label_showresult = QtWidgets.QLabel(self.centralwidget)
        self.label_showresult.setGeometry(QtCore.QRect(260, 460, 161, 211))
        self.label_showresult.setStyleSheet("font: 14pt \"黑体\";\n"
"background-color: rgba(85, 170, 255, 0);\n"
"color: rgb(85, 170, 255);")
        self.label_showresult.setText("")
        self.label_showresult.setObjectName("label_showresult")
        self.horizontalSlider_laser = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_laser.setGeometry(QtCore.QRect(90, 250, 131, 22))
        self.horizontalSlider_laser.setProperty("value", 18)
        self.horizontalSlider_laser.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_laser.setObjectName("horizontalSlider_laser")
        self.spinBox_laser = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_laser.setGeometry(QtCore.QRect(10, 250, 42, 22))
        self.spinBox_laser.setProperty("value", 18)
        self.spinBox_laser.setObjectName("spinBox_laser")
        self.label_show_tongkong_video = QtWidgets.QLabel(self.centralwidget)
        self.label_show_tongkong_video.setGeometry(QtCore.QRect(250, 200, 641, 481))
        self.label_show_tongkong_video.setText("")
        self.label_show_tongkong_video.setObjectName("label_show_tongkong_video")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"font: 14pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"font: 14pt \"黑体\";")
        self.label_4.setObjectName("label_4")
        self.spinBox_wuxiang = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_wuxiang.setGeometry(QtCore.QRect(10, 340, 42, 22))
        self.spinBox_wuxiang.setObjectName("spinBox_wuxiang")
        self.horizontalSlider_wuxiang = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_wuxiang.setGeometry(QtCore.QRect(90, 340, 131, 22))
        self.horizontalSlider_wuxiang.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_wuxiang.setObjectName("horizontalSlider_wuxiang")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 390, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"font: 14pt \"黑体\";")
        self.label_5.setObjectName("label_5")
        self.horizontalSlider_huanxingdeng_out = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_huanxingdeng_out.setGeometry(QtCore.QRect(90, 430, 131, 22))
        self.horizontalSlider_huanxingdeng_out.setProperty("value", 36)
        self.horizontalSlider_huanxingdeng_out.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_huanxingdeng_out.setObjectName("horizontalSlider_huanxingdeng_out")
        self.spinBox_huanxingdeng_out = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_huanxingdeng_out.setGeometry(QtCore.QRect(10, 430, 42, 22))
        self.spinBox_huanxingdeng_out.setProperty("value", 36)
        self.spinBox_huanxingdeng_out.setObjectName("spinBox_huanxingdeng_out")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 470, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"font: 14pt \"黑体\";")
        self.label_6.setObjectName("label_6")
        self.horizontalSlider_huanxingdeng_in = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_huanxingdeng_in.setGeometry(QtCore.QRect(90, 510, 131, 22))
        self.horizontalSlider_huanxingdeng_in.setProperty("value", 14)
        self.horizontalSlider_huanxingdeng_in.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_huanxingdeng_in.setObjectName("horizontalSlider_huanxingdeng_in")
        self.spinBox_huanxingdeng_in = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_huanxingdeng_in.setGeometry(QtCore.QRect(10, 510, 42, 22))
        self.spinBox_huanxingdeng_in.setProperty("value", 14)
        self.spinBox_huanxingdeng_in.setObjectName("spinBox_huanxingdeng_in")
        self.pushButton_closecamer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_closecamer.setGeometry(QtCore.QRect(940, 130, 75, 23))
        self.pushButton_closecamer.setObjectName("pushButton_closecamer")
        self.pushButton_capture_hateman = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_capture_hateman.setGeometry(QtCore.QRect(670, 80, 131, 23))
        self.pushButton_capture_hateman.setObjectName("pushButton_capture_hateman")
        self.label_show_hateman_video = QtWidgets.QLabel(self.centralwidget)
        self.label_show_hateman_video.setGeometry(QtCore.QRect(230, 180, 641, 481))
        self.label_show_hateman_video.setText("")
        self.label_show_hateman_video.setObjectName("label_show_hateman_video")
        self.pushButton_switch_to_tongkong = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_switch_to_tongkong.setGeometry(QtCore.QRect(214, 80, 61, 23))
        self.pushButton_switch_to_tongkong.setObjectName("pushButton_switch_to_tongkong")
        self.pushButton_switch_to_hateman = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_switch_to_hateman.setGeometry(QtCore.QRect(610, 80, 61, 23))
        self.pushButton_switch_to_hateman.setObjectName("pushButton_switch_to_hateman")
        self.label_show_jiaomo = QtWidgets.QLabel(self.centralwidget)
        self.label_show_jiaomo.setGeometry(QtCore.QRect(730, 480, 121, 151))
        self.label_show_jiaomo.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(85, 170, 255);\n"
"font: 14pt \"黑体\";")
        self.label_show_jiaomo.setText("")
        self.label_show_jiaomo.setObjectName("label_show_jiaomo")
        self.pushButton_history = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_history.setGeometry(QtCore.QRect(940, 80, 75, 23))
        self.pushButton_history.setObjectName("pushButton_history")
        self.pushButton_inputname = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inputname.setGeometry(QtCore.QRect(680, 30, 75, 23))
        self.pushButton_inputname.setObjectName("pushButton_inputname")
        self.spinBox_up = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_up.setGeometry(QtCore.QRect(950, 330, 51, 31))
        self.spinBox_up.setMaximum(480)
        self.spinBox_up.setSingleStep(5)
        self.spinBox_up.setProperty("value", 320)
        self.spinBox_up.setObjectName("spinBox_up")
        self.spinBox_right = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_right.setGeometry(QtCore.QRect(1030, 330, 51, 31))
        self.spinBox_right.setMaximum(640)
        self.spinBox_right.setSingleStep(5)
        self.spinBox_right.setProperty("value", 240)
        self.spinBox_right.setObjectName("spinBox_right")
        self.pushButton_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zero.setGeometry(QtCore.QRect(940, 230, 75, 23))
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_forward = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_forward.setGeometry(QtCore.QRect(970, 420, 75, 23))
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.pushButton_backward = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_backward.setGeometry(QtCore.QRect(970, 480, 75, 23))
        self.pushButton_backward.setObjectName("pushButton_backward")
        self.pushButton_opencamer.raise_()
        self.pushButton_caculate.raise_()
        self.horizontalSlider_laser.raise_()
        self.spinBox_laser.raise_()
        self.label_show_tongkong_video.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.spinBox_wuxiang.raise_()
        self.horizontalSlider_wuxiang.raise_()
        self.label_5.raise_()
        self.horizontalSlider_huanxingdeng_out.raise_()
        self.spinBox_huanxingdeng_out.raise_()
        self.label_6.raise_()
        self.horizontalSlider_huanxingdeng_in.raise_()
        self.spinBox_huanxingdeng_in.raise_()
        self.pushButton_closecamer.raise_()
        self.pushButton_capture_hateman.raise_()
        self.pushButton_switch_to_tongkong.raise_()
        self.pushButton_switch_to_hateman.raise_()
        self.label_show_hateman_video.raise_()
        self.label_show_jiaomo.raise_()
        self.label_showresult.raise_()
        self.pushButton_history.raise_()
        self.pushButton_inputname.raise_()
        self.spinBox_up.raise_()
        self.spinBox_right.raise_()
        self.pushButton_zero.raise_()
        self.pushButton_forward.raise_()
        self.pushButton_backward.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 23))
        self.menubar.setObjectName("menubar")
        self.menu_test = QtWidgets.QMenu(self.menubar)
        self.menu_test.setObjectName("menu_test")
        self.menu_history = QtWidgets.QMenu(self.menubar)
        self.menu_history.setObjectName("menu_history")
        self.menu_set = QtWidgets.QMenu(self.menubar)
        self.menu_set.setObjectName("menu_set")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_test.menuAction())
        self.menubar.addAction(self.menu_history.menuAction())
        self.menubar.addAction(self.menu_set.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_opencamer.setText(_translate("MainWindow", "打开瞳孔摄像头"))
        self.pushButton_caculate.setText(_translate("MainWindow", "测量"))
        self.label_3.setText(_translate("MainWindow", "激光灯"))
        self.label_4.setText(_translate("MainWindow", "物象灯"))
        self.label_5.setText(_translate("MainWindow", "环形灯_外"))
        self.label_6.setText(_translate("MainWindow", "环形灯_内"))
        self.pushButton_closecamer.setText(_translate("MainWindow", "退出"))
        self.pushButton_capture_hateman.setText(_translate("MainWindow", "打开hateman摄像头"))
        self.pushButton_switch_to_tongkong.setText(_translate("MainWindow", "切换至"))
        self.pushButton_switch_to_hateman.setText(_translate("MainWindow", "切换至"))
        self.pushButton_history.setText(_translate("MainWindow", "历史记录"))
        self.pushButton_inputname.setText(_translate("MainWindow", "输入姓名"))
        self.pushButton_zero.setText(_translate("MainWindow", "保存零位"))
        self.pushButton_forward.setText(_translate("MainWindow", "up"))
        self.pushButton_backward.setText(_translate("MainWindow", "down"))
        self.menu_test.setTitle(_translate("MainWindow", "测试"))
        self.menu_history.setTitle(_translate("MainWindow", "历史记录"))
        self.menu_set.setTitle(_translate("MainWindow", "设置"))

