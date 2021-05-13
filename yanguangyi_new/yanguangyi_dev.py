from PyQt5.QtGui import QPixmap
from fun import bujindianji_Z
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time
import numpy as np
from dev_win import Ui_MainWindow
class dev_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 父类的构造函数
        self.setupUi(self)
        self.initslot()

    def initslot(self):
        self.pushButton_Z_UP.clicked.connect(self.Z_UP)
        self.pushButton_Z_DOWN.clicked.connect(self.Z_DOWN)

        # self.run()
    def Z_UP(self):
        bujindianji_Z.backward(0.00001, 200)
    def Z_DOWN(self):
        bujindianji_Z.forward(0.00001, 200)

    # def run(self):
    #
    #
    #     while bujindianji_Z.xianwei_switch.is_active:
    #         try:
    #               biase = np.loadtxt("biase.txt")
    #
    #               # print(biase[1])
    #               step = int(abs(biase[1])*5.55)
    #               if biase[1] > 0:  ####圆环中心在下面, 上下
    #                   if 5 <abs(biase[1]) < 180:
    #                       time.sleep(10)
    #                       bujindianji_Z.forward(0.00000001, step)
    #                       # bujindianji_Z.backward(0.00000001, step)
    #                       # bujindianji_Z.forward(0.000001, int(step / 4))
    #                       # bujindianji_Z.forward(0.00001, int(step / 8))
    #                       # bujindianji_Z.forward(0.0001, int(step / 8))
    #
    #                   # if 14 < biase < 101:
    #                   #
    #                   #     bujindianji_Z.forward(0.000000001, 60)
    #                   # if 5 < biase < 15:
    #                   #
    #                   #     bujindianji_Z.forward(0.000000001, 5)
    #
    #                   else:
    #                       bujindianji_Z.stop()
    #               if biase[1] < 0:  ####圆环中心在上面
    #                   if 5 <abs(biase[1]) < 180:
    #
    #                       bujindianji_Z.backward(0.00000001, step)
    #
    #                   # if 14 < biase < 101:
    #                   #
    #                   #     bujindianji_Z.forward(0.000000001, 60)
    #                   # if 5 < biase < 15:
    #                   #
    #                   #     bujindianji_Z.forward(0.000000001, 5)
    #
    #                   else:
    #                       bujindianji_Z.stop()
    #
    #         except:
    #             print("1")
    #         time.sleep(10)
    #
    #
    #
    #     else:
    #         bujindianji_Z.stop()
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
#     win_dev = dev_window()
#     win_dev.run()
#     win_dev.show()
#     sys.exit(app.exec_())