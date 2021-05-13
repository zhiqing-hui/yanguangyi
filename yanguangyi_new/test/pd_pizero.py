# from gpiozero import Button
#
# btn = Button(4, pull_up=True)
#
# btn.wait_for_active()
# print("button was pressed")

from gpiozero import PWMLED, Button, LED
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import time
import numpy as np


class TestWindow(QDialog):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("Start", self)
        btn2 = QPushButton("Stop", self)
        self.sec_label = QLabel(self)
        # self.sensor_pd = Button(4)  #####buttun默认 is_active
        layout = QGridLayout(self)
        layout.addWidget(btn1, 0, 0)
        layout.addWidget(btn2, 0, 1)
        layout.addWidget(self.sec_label, 1, 0, 1, 2)
        self.sum_pd_move = 1
        # self.timer_pd = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        # self.timer_pd.start(30)
        # self.sensor_pd = Button(4)  #####buttun默认 is_active
        self.thread = Thread_PD()
        #   # 线程发过来的信号挂接到槽：update
        self.thread.pd_changed_signal.connect(self.update_pd)
        btn1.clicked.connect(self.thread.start)
        btn2.clicked.connect(self.thread.terminate)  # 线程中止
        # btn2.clicked.connect(self.restart_pd)  # 线程中止
        # self.timer_pd.timeout.connect(self.run)

    def update_pd(self, num):


        self.sum_pd_move = self.sum_pd_move + num

        self.sec_label.setText(str(self.sum_pd_move))

    def restart_pd(self):
        self.sum_pd_move = 0


# class MyThread(QThread):
#     sec_changed_signal = pyqtSignal(int)  # 信号类型：int
#
#     def __init__(self, sec=1000, parent=None):
#         super().__init__(parent)
#         self.sec = sec  # 默认1000秒
#
#     def run(self):
#         for i in range(self.sec):
#             self.sec_changed_signal.emit(i)  # 发射信号
#             time.sleep(1)
class Thread_PD(QThread):
    pd_changed_signal = pyqtSignal(int)
    def __init__(self,parent = None):
        super().__init__(parent)
        self.sensor_pd = Button(8)  #####buttun默认 is_active

    def run(self):
        # self.initial_status = self.sensor_pd.value
        while True:
            self.sensor_pd.wait_for_active()
            self.sensor_pd.wait_for_inactive()
            print(self.sensor_pd.value)
            self.emitsignal()
            # time.sleep(0.1)

    def pressed(self):
        print("pressed")
    def emitsignal(self):
        self.pd_changed_signal.emit(1)
#
#
    # def run(self):
    #     # self.initial_status = self.sensor_pd.value
    #     if:
    #         self.sensor_pd.wait_for_active()
    #         self.sensor_pd.wait_for_inactive()
    #         print(self.sensor_pd.value)
app = QApplication(sys.argv)
form = TestWindow()
form.show()
app.exec_()