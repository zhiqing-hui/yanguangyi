import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
# from gpiozero import PWMLED, Button, LED
# from gpiozero.pins.pigpio import *
# from gpiozero.pins.rpigpio import *

# import cv2
# from fun import fun_for_yanguangyi   ####核心算法模块
# from fun import fun_for_zhixin
# from PyQt5.QtGui import QPixmap
# # from picamera import PiCamera
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_win import Ui_MainWindow  ###3导入主窗口UI
from yangungyi_custom_menu import menu_win ####导入菜单窗口
# from yanguangyi_develop import test_window ####导入开发者界面
# import xlrd                           #导入读取表格模块
# from xlutils.copy import copy        #导入copy模块
# import time
# from fun import bujindianji_wuxiang
# from fun import bujindianji_Z
# from fun import laser
# from fun import yuanhuandeng
# from fun import yunguangdianji
# from fun import wuxiangdeng
# import pd_pizero
# from fun import tcp_server
# from yanguangyi_dev import dev_window


biase = np.zeros(3)  ####存储三轴位置偏差
finalresult = np.zeros(6)  ####存储测量结果
mouse_move = np.array([0, 0])
class main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 父类的构造函数
        self.setupUi(self)
#         self.sum_pd_move = 0
#         self.num_jinshi = 100  ####近视哈特曼阈值
#         self.standard_R = 145  ####标准瞳孔大小（像素值）
#         self.PIX_R1 = 17.8  ####圆环半径转换系数
#         self.PIX_R2 = 17.8  ####圆环半径转换系数
#         self.num = 0.0045  #####实际质心位置与质心像素坐标转换系数
#
#         self.initrow = 0
#         self.times_caculate = 0
#
#         self.result_tongkong = np.zeros(3)
#         self.SPH = np.zeros(5)  ####保存球镜度
#         self.CYL = np.zeros(5)  ####保存柱镜度
#         self.A = np.zeros(5)  ####保存轴位
#         self.R1 = np.zeros(5)  ####保存R1
#         self.R2 = np.zeros(5)  ####保存R2
#         self.Axis = np.zeros(5)  ####保存Axis
#         self.SPH_ALL = np.zeros(5)  ####保存5次球镜度
#         self.CYL_ALL = np.zeros(5)  ####保存5次柱镜度
#         self.A_ALL = np.zeros(5)  ####保存5次轴位
#         self.R1_ALL = np.zeros(5)  ####保存5次R1
#         self.R2_ALL = np.zeros(5)  ####保存5次R2
#         self.Axis_ALL = np.zeros(5)  ####保存5次Axis
#         self.final_result = np.zeros(6)   ####保存最终结果
#
#         self.yuanhuan_x = 320
#         self.yuanhuan_y = 240
#         self.timer_camera_tongkong = QtCore.QTimer()
#         self.timer_camera_hateman = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
#         self.timer_button = QtCore.QTimer()
#         self.timer_caculate_zero = QtCore.QTimer()
#
#         self.cap_tongkong = cv2.VideoCapture()
#         self.cap_hateman = cv2.VideoCapture()  # 视频流
#
#
#         self.CAM_TONGKONG = 0 #为0时表示视频流来自笔记本内置摄像头
#         self.CAM_HATEMAN = 2
#
#         self.zernike = np.loadtxt("./tempfile_txt/zernike_r_l_1_3_25.txt",
#                              dtype=np.float32)
#
#
#         ##########光路电子器件控制##############
#         laser.laser_on(0.22)
#         yuanhuandeng.yuanhuandeng_on(0.2, 0.2)
#         wuxiangdeng.wuxiangdeng_on(0.35)
#         yunguangdianji.yunguangdianji_on()
#
#         self.buttun_test = Button(25)   ####测试按钮
#
#
#
#
#
#         # self.thread_caculate_zero = Thread_caculate_zero()  ####瞳距
#
#
#
#         self.slot_init()  # 初始化槽函数t自带的，会关闭程序
#         self.label_show_pic.mousePressEvent = self.mouseMoveEvent
#     def slot_init(self):
#
#         # self.thread_pd_change.pd_changed_signal.connect(self.update_pd)
#
#         self.timer_camera_tongkong.timeout.connect(self.show_camera_tongkong)  # 若定时器结束，则调用show_camera()
#         self.timer_camera_hateman.timeout.connect(self.show_camera_hateman)  # 若定时器结束，则调用show_camera()
#         self.pushButton_show_diantu.clicked.connect(self.show_hateman_pic)
#         self.pushButtun_close_hateman.clicked.connect(self.hide_hateman_pic)
#         self.timer_button.timeout.connect(self.M_button_pressed)
#
#
#
#         self.comboBox_MODE_result.activated[str].connect(self.MODE_RESULT)    ####测量模式复选框
#         self.pushButton_close_history.clicked.connect(self.history_table_hide)
#         self.pushButton_HIS.clicked.connect(self.history_table_show)
#         self.pushButton_clear_history.clicked.connect(self.clear_history_table)
#
#
#         # self.timer_caculate_zero.timeout.connect(self.caculate_zero)
#     # def button_click(self):
#     #     if self.buttun.is_active:
#     #         print("button is clicked")
#     #         self.caculate()
#     def show_hateman_pic(self):
#         try:
#            show1 = cv2.resize(self.img_jinshi_gray, (420, 280))  # 把读到的帧的大小重新设置为 640x480
#
#            showImage = QtGui.QImage(show1.data, show1.shape[1], show1.shape[0],
#                                     QtGui.QImage.Format_Grayscale8)  # 把读取到的视频数据变成QImage形式
#            self.label_showhateman.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
#            self.label_showhateman.show()
#            self.pushButtun_close_hateman.show()
#
#         except:
#             msg = QtWidgets.QMessageBox.warning(self, 'warning', "请先测量", buttons=QtWidgets.QMessageBox.Ok)
#
#     def MODE_RESULT(self, index):
#         if(index == "REF"):
#             self.REF_MODE()
#
#         if (index == "KER"):
#             self.KER_MODE()
#
#         if (index == "R/K"):
#             self.R_K_MODE()
#
#     def start_hide(self):
#         self.label_showhateman.hide()  ####显示哈特慢图的窗口默认隐藏
#         self.pushButtun_close_hateman.hide()  ####关闭哈特慢图的按钮默认隐藏
#         self.tableWidget_history.hide()      ####历史记录表格隐藏
#         self.pushButton_close_history.hide()  ####隐藏关闭历史记录表格按钮隐藏
#         self.pushButton_clear_history.hide()  ####隐藏清除历史记录表格按钮隐藏
#         ####hide_R1_R2_Axis_L####
#         self.label_9.hide()
#         self.label_10.hide()
#         self.label_11.hide()
#         ####hide_R1_R2_Axis_R####
#         self.label_12.hide()
#         self.label_13.hide()
#         self.label_14.hide()
#         ####hide_value_R1_R2_Axis_L####
#         self.label_L_R1.hide()
#         self.label_L_R2.hide()
#         self.label_L_Axis.hide()
#         ####hide_value_R1_R2_Axis_R####
#         self.label_R_R1.hide()
#         self.label_R_R2.hide()
#         self.label_R_Axis.hide()
#     def KER_MODE(self):
#
#
#         ###########################隐藏屈光度测试结果#######################
#         ####show_S_C_A_R#####
#         self.label_3.hide()  ##S
#         self.label_4.hide()  ##C
#         self.label_5.hide()  ##A
#         ####show_S_C_A_L#####
#         self.label_6.hide()  ##C
#         self.label_7.hide()  ##S
#         self.label_8.hide()  ##A
#
#         ####show_value_S_C_A_R#####
#         self.label_L_S.hide()  ##S
#         self.label_L_C.hide()  ##C
#         self.label_L_A.hide()  ##A
#         ####show_value_S_C_A_L#####
#         self.label_R_S.hide()  ##S
#         self.label_R_C.hide()  ##C
#         self.label_R_A.hide()  ##A
#
#
#         #################################显示角膜测量结果###################
#         self.label_9.show()
#         self.label_10.show()
#         self.label_11.show()
#         ####hide_R1_R2_Axis_R####
#         self.label_12.show()
#         self.label_13.show()
#         self.label_14.show()
#         ####hide_value_R1_R2_Axis_L####
#         self.label_L_R1.show()
#         self.label_L_R2.show()
#         self.label_L_Axis.show()
#         ####hide_value_R1_R2_Axis_R####
#         self.label_R_R1.show()
#         self.label_R_R2.show()
#         self.label_R_Axis.show()
#     def REF_MODE(self):
#
#         ###########################显示屈光度测试结果#######################
#         ####show_S_C_A_R#####
#         self.label_3.show()  ##S
#         self.label_4.show()  ##C
#         self.label_5.show()  ##A
#         ####show_S_C_A_L#####
#         self.label_6.show()  ##C
#         self.label_7.show()  ##S
#         self.label_8.show()  ##A
#
#         ####show_value_S_C_A_R#####
#         self.label_L_S.show()  ##S
#         self.label_L_C.show()  ##C
#         self.label_L_A.show()  ##A
#         ####show_value_S_C_A_L#####
#         self.label_R_S.show()  ##S
#         self.label_R_C.show()  ##C
#         self.label_R_A.show()  ##A
#
#
#
#         #################################隐藏角膜测量结果###################
#         self.label_9.hide()
#         self.label_10.hide()
#         self.label_11.hide()
#         ####hide_R1_R2_Axis_R####
#         self.label_12.hide()
#         self.label_13.hide()
#         self.label_14.hide()
#         ####hide_value_R1_R2_Axis_L####
#         self.label_L_R1.hide()
#         self.label_L_R2.hide()
#         self.label_L_Axis.hide()
#         ####hide_value_R1_R2_Axis_R####
#         self.label_R_R1.hide()
#         self.label_R_R2.hide()
#         self.label_R_Axis.hide()
#     def R_K_MODE(self):
#         ###########################显示屈光度测试结果#######################
#         ####show_S_C_A_R#####
#         self.label_3.show()  ##S
#         self.label_4.show()  ##C
#         self.label_5.show()  ##A
#         ####show_S_C_A_L#####
#         self.label_6.show()  ##C
#         self.label_7.show()  ##S
#         self.label_8.show()  ##A
#
#         ####show_value_S_C_A_R#####
#         self.label_L_S.show()  ##S
#         self.label_L_C.show()  ##C
#         self.label_L_A.show()  ##A
#         ####show_value_S_C_A_L#####
#         self.label_R_S.show()  ##S
#         self.label_R_C.show()  ##C
#         self.label_R_A.show()  ##A
#
#         #################################显示角膜测量结果###################
#         self.label_9.show()
#         self.label_10.show()
#         self.label_11.show()
#         ####hide_R1_R2_Axis_R####
#         self.label_12.show()
#         self.label_13.show()
#         self.label_14.show()
#         ####hide_value_R1_R2_Axis_L####
#         self.label_L_R1.show()
#         self.label_L_R2.show()
#         self.label_L_Axis.show()
#         ####hide_value_R1_R2_Axis_R####
#         self.label_R_R1.show()
#         self.label_R_R2.show()
#         self.label_R_Axis.show()
#
#
#     def hide_hateman_pic(self):
#         self.label_showhateman.hide()
#         self.pushButtun_close_hateman.hide()
#     def autorun(self):
#         # cam1 = multiprocessing.Process(target=self.button_open_camera_tongkong_clicked, args=(0,))
#         # cam1.start()
#
#         self.button_open_camera_hateman_clicked(2)  #####打开哈特慢摄像头
#         self.caculate_zero()
#         self.start_hide()
#         self.button_open_camera_tongkong_clicked(self.CAM_TONGKONG)  #####打开瞳孔摄像头
#         # self.label_showhateman.hide()  ####显示哈特慢图的窗口默认隐藏
#         # self.pushButtun_close_hateman.hide()  ####关闭哈特慢图的按钮默认隐藏
#         # cam2 = multiprocessing.Process(target=self.button_open_camera_hateman_clicked, args=(self.CAM_HATEMAN,))
#         # cam2.start()
#
#
#         self.timer_button.start(200)####每隔0.03秒检测按钮是否被按下
#         # self.timer_bujindianji_Z.start(200)  ####
#
#         # self.timer_caculate_zero.start(500)  ####每隔0.03秒检测按钮是否被按下
#     def button_open_camera_tongkong_clicked(self, port):
#
#         if self.timer_camera_tongkong.isActive() == False:  # 若定时器未启动
#             flag = self.cap_tongkong.open(port)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
#             self.cap_tongkong.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))  # 视频流格式
#             self.cap_tongkong.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#             self.cap_tongkong.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#             if flag == False:  # flag表示open()成不成功
#                 msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查瞳孔相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
#             else:
#                 self.timer_camera_tongkong.start(30) # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
#                 self.diaoyong_Z_jiange = 0
#
#                 # self.pushButton.setText('（关闭）瞳孔相机')
#         else:
#             self.timer_camera_tongkong.stop()  # 关闭定时器
#             self.cap_tongkong.release()  # 释放视频流
#             # self.label_show_pic.clear()  # 清空视频显示区域
#             # self.pushButton_opencame.setText('打开瞳孔相机')      da      ####################
#     def show_camera_tongkong(self):
#
#         flag, self.image2 = self.cap_tongkong.read()  # 从视频流中读取
#
#
#
#
#
#         show1 = cv2.resize(self.image2, (640, 480))  # 把读到的帧的大小重新设置为 640x480
#         show2 = cv2.cvtColor(show1, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
#         show2 = cv2.flip(show2, 1)             ####左右翻转
#         show2 = cv2.flip(show2, 0)             ####上下翻转
#         show3 = cv2.cvtColor(show2, cv2.COLOR_RGB2GRAY)
#         show4 = cv2.GaussianBlur(show3, (5, 5), 1)
#         cv2.circle(show2, (self.yuanhuan_x, self.yuanhuan_y), 30, (255, 255, 127), 2)
#         cv2.line(show2, (self.yuanhuan_x - 20, self.yuanhuan_y), (self.yuanhuan_x + 20, self.yuanhuan_y), (255, 255, 127),
#                  2)
#         cv2.line(show2, (self.yuanhuan_x, self.yuanhuan_y - 20), (self.yuanhuan_x, self.yuanhuan_y + 20), (255, 255, 127),
#                  2)
#         ret, show5 = cv2.threshold(show4, 100, 255, cv2.THRESH_BINARY)
#         show6 = cv2.Canny(show5, 40, 255)
#         contours, hierarchy = cv2.findContours(show6, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#         save_big = []  # 存储合理大轮廓
#         rectall_big = []  # 存储对应大轮廓的在最小面积矩形
#
#
#         for contour in contours:
#
#             rect = cv2.minAreaRect(contour)
#
#             if fun_for_yanguangyi.verifySizes_big_circle(rect):####满足大轮廓条件
#                 save_big.append(contour)
#
#                 rectall_big.append(rect)
#
#
#         # cnt = contours[4]
#         # print(len(save))
#
#         if len(save_big) == 0:   ####确保无人测量时电机不会运作
#             bujindianji_Z.stop()
#             # self.biase[0] = 0
#             # self.biase[1] = 0
#             # self.biase[2] = 0
#             global biase
#             biase[0] = 0
#             biase[1] = 0
#             biase[2] = 0
#             # np.savetxt("./tempfile_txt/biase.txt", self.biase, fmt='%s')
#         for finalcontour in save_big:
#             # global biase
#
#             ellipse = cv2.fitEllipse(finalcontour)
#             self.ellipse_center_x_biase = int(ellipse[0][0]) - self.yuanhuan_x
#             self.ellipse_center_y_biase = int(ellipse[0][1]) - self.yuanhuan_y
#             biase[0] = self.ellipse_center_x_biase  ####左右偏移(像素值)
#             biase[1] = self.ellipse_center_y_biase   ####上下偏移(像素值)
#
#
#
#             self.R1_tem = ellipse[1][0]
#             self.R2_tem = ellipse[1][1]
#             self.Axis_tem = ellipse[2]
#             biase[2] = (self.R1_tem + self.R2_tem)/2  ####前后偏移（像素值）
#
#             # np.savetxt("./tempfile_txt/biase.txt", self.biase, fmt='%s')
#             if abs(biase[1]) > 10:
#                 self.times_caculate = 0
#
#             if biase[0] in range(-5, 5) and biase[1] in range(-5, 5):
#
#                 self.Auto_caculate(self.R1_tem, self.R2_tem, self.Axis_tem)
#
#
#                 cv2.circle(show2, (self.yuanhuan_x, self.yuanhuan_y), 30, (255, 255, 0), 2)
#                 cv2.line(show2, (self.yuanhuan_x - 20, self.yuanhuan_y), (self.yuanhuan_x + 20, self.yuanhuan_y),
#                          (0, 255, 0), 2)
#                 cv2.line(show2, (self.yuanhuan_x, self.yuanhuan_y - 20), (self.yuanhuan_x, self.yuanhuan_y + 20),
#                          (0, 255, 0), 2)
#                 # cv2.putText(show2, text, (70, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
#                 cv2.drawContours(show2, save_big, -1, (0, 0, 255), 1)
#
#         showImage = QtGui.QImage(show2.data, show2.shape[1], show2.shape[0],
#                                  QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
#         self.label_show_pic.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
#
#
#     def mouseMoveEvent(self, event):     ####获取鼠标点击位置
#         s = event.pos()
#         global mouse_move
#         mouse_move[0] = s.x()-320
#         mouse_move[1] = s.y()-240
#
#
#
#
#
#
#
#
#
#
#
#     def button_open_camera_hateman_clicked(self, port):
#
#
#         if self.timer_camera_hateman.isActive() == False:  # 若定时器未启动
#             flag = self.cap_hateman.open(port)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
#             self.cap_hateman.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))  # 视频流格式
#             self.cap_hateman.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#             self.cap_hateman.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
#             if flag == False:  # flag表示open()成不成功
#                 msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查哈特曼相机于电脑是否连接正确",
#                                                     buttons=QtWidgets.QMessageBox.Ok)
#             else:
#                 self.timer_camera_hateman.start(30)# 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
#
#                 # self.pushButton_capture_hateman.setText('(关闭)hateman相机')
#         else:
#             self.timer_camera_hateman.stop()  # 关闭定时器
#             self.cap_hateman.release()  # 释放视频流
#             # self.label_show_hateman_video.clear()  # 清空视频显示区域
#             # self.pushButton_capture_hateman.setText('打开hateman相机')
#
#     def show_camera_hateman(self):
#
#         flag, self.image = self.cap_hateman.read()  # 从视频流中读取
#
#         self.show0 = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
#
#
#
#         # file_savepath_jinshi = str(self.text) + ".bmp"
#
#         # if self.buttun.is_active:
#         #     self.caculate()
#             # cv2.imwrite(file_savepath_jinshi, self.show)
#
#         # showImage = QtGui.QImage(self.show_hateman.data, self.show_hateman.shape[1], self.show_hateman.shape[0],
#         #                          QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
#         # self.label_show_hateman_video.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
#
#     def caculate_zero(self):
#         num_zero = 180
#         img_zero = cv2.imread("./pic/0.bmp", 0)
#
#         ret, self.img_zero_gray = cv2.threshold(img_zero, num_zero, 255, cv2.THRESH_TOZERO)
#         self.zero_ellipse = fun_for_zhixin.caculate_center(self.img_zero_gray)  ####计算零位质心
#                                                ######打开激光灯
#     def caculate(self, img_jinshi):
#
#         self.jinshi_ellipse = fun_for_zhixin.caculate_center(img_jinshi)  ####计算近视质心
#
#         SPH = 0.83 * (self.jinshi_ellipse[1][0] - self.zero_ellipse[1][0])
#         if abs(self.jinshi_ellipse[1][0]-self.jinshi_ellipse[1][1]) <= 5:
#             CYL = 0.00
#             Axis = 180.00
#         else:
#             CYL = -3.00
#             Axis = self.jinshi_ellipse[3] - 90.00
#         quguangdu_result = np.zeros([3, 1], dtype=np.float32)
#         quguangdu_result[0] = SPH
#         quguangdu_result[1] = CYL
#         quguangdu_result[2] = Axis
#         return quguangdu_result
#
#         # if biase < 0 and abs(biase) < 18:
#         #
#         #     return biase
#         # if biase < 0 and abs(biase) > 18:
#         #     return 1.06 * biase
#         # if biase > 0 and abs(biase) <= 4:
#         #     return 0.75 * biase
#         # if biase > 0 and 4 < abs(biase) < 26:
#         #     return 0.7 * biase
#
#
#
#
#
#     def show_finalresult_L(self, result):
#
#         #### left eye##########################
#         ####显示屈光度测试结果
#         self.label_L_S.setText("%.2f" % (result[0]))
#         self.label_L_C.setText("%.2f" % (result[1]))
#         self.label_L_A.setText("%.2f" % (result[2]))
#
#         ####显示角膜测试结果
#         self.label_L_R1.setText("%.2f" % (result[3]))
#         self.label_L_R2.setText("%.2f" % (result[4]))
#         self.label_L_Axis.setText("%.2f" % (result[5]))
#
#     def show_finalresult_R(self, result):
#         #### right eye############################
#         ####显示屈光度测试结果
#         self.label_R_S.setText("%.2f" % (result[0]))
#         self.label_R_C.setText("%.2f" % (result[1]))
#         self.label_R_A.setText("%.2f" % (result[2]))
#         self.lijiao = self.result[0]
#         ####显示角膜测试结果
#         self.label_R_R1.setText("%.2f" % (result[3]))
#         self.label_R_R2.setText("%.2f" % (result[4]))
#         self.label_R_Axis.setText("%.2f" % (result[5]))
#
#     def write_to_history_table(self, result):
#
#         newItem = QTableWidgetItem("%.2f" % (result[0]))  # 创建表格项---文本项目
#         self.tableWidget_history.setItem(self.initrow, 0, newItem)  # 给指定单元格设置数据
#         newItem = QTableWidgetItem("%.2f" % (result[1]))
#         self.tableWidget_history.setItem(self.initrow, 1, newItem)
#         newItem = QTableWidgetItem("%.2f" % (result[2]))
#         self.tableWidget_history.setItem(self.initrow, 2, newItem)
#         newItem = QTableWidgetItem("%.2f" % (result[3]))
#         self.tableWidget_history.setItem(self.initrow, 3, newItem)
#         newItem = QTableWidgetItem("%.2f" % (result[4]))
#         self.tableWidget_history.setItem(self.initrow, 4, newItem)
#         newItem = QTableWidgetItem("%.2f" % (result[5]))
#         self.tableWidget_history.setItem(self.initrow, 5, newItem)
#         self.initrow = self.initrow + 1
#
#
#     def clear_history_table(self):
#         self.initrow = 0
#         for rownum in range(0, self.tableWidget_history.rowCount()):
#             # self.tableWidget_history.removeRow(rownum)
#             newItem = QTableWidgetItem("")  # 创建表格项---文本项目
#             self.tableWidget_history.setItem(rownum, 0, newItem)  # 给指定单元格设置数据
#             newItem = QTableWidgetItem("")  # 创建表格项---文本项目
#             self.tableWidget_history.setItem(rownum, 1, newItem)
#             newItem = QTableWidgetItem("")  # 创建表格项---文本项目
#             self.tableWidget_history.setItem(rownum, 2, newItem)
#             newItem = QTableWidgetItem("")  # 创建表格项---文本项目
#             self.tableWidget_history.setItem(rownum, 3, newItem)
#             newItem = QTableWidgetItem("")  # 创建表格项---文本项目
#             self.tableWidget_history.setItem(rownum, 4, newItem)
#             newItem = QTableWidgetItem("")  # 创建表格项---文本项目
#             self.tableWidget_history.setItem(rownum, 5, newItem)
#
#     def history_table_hide(self):
#         self.tableWidget_history.hide()
#
#         self.pushButton_close_history.hide()    ####隐藏关闭按钮
#         self.pushButton_clear_history.hide()    ####隐藏清除按钮
#     def history_table_show(self):
#         self.tableWidget_history.show()
#         self.pushButton_close_history.show()    ####显示关闭按钮
#         self.pushButton_clear_history.show()    ####显示清除按钮
#
#
#
#     def M_button_pressed(self):    ####按钮被按下后的操作
#
#         if self.buttun_test.is_active:
#             try:
#             #    time.sleep(1)
#             ##########save pic_hateman########
#                 self.show_hateman_rgb = cv2.cvtColor(self.show0, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
#                 self.show_hateman = cv2.cvtColor(self.show_hateman_rgb, cv2.COLOR_RGB2GRAY)
#                 ret2, self.img_jinshi_gray = cv2.threshold(self.show_hateman, self.num_jinshi, 255, cv2.THRESH_BINARY)
#                 cv2.imwrite("./pic/jinshi_thresh_" + str(self.times_caculate) + ".bmp", self.img_jinshi_gray)
#                 cv2.imwrite("./pic/jinshi_gray_" + str(self.times_caculate) + ".bmp", self.show_hateman)
#                 quguangdu = self.caculate(self.img_jinshi_gray)  ####计算屈光度
#                 print(quguangdu)
#             except:
#                 msg = QtWidgets.QMessageBox.warning(self, 'warning', "屈光度错误",
#                                                      buttons=QtWidgets.QMessageBox.Ok)
#             # self.label_L_R1.setText("%.2f" % (self.R1 / self.PIX_R1))
#             # self.label_L_R2.setText("%.2f" % (self.R2 / self.PIX_R2))
#             # self.label_L_Axis.setText("%.2f" % (self.Axis))
#             # self.laser.value = 0
#             # self.write_to_history_table()
#
#
#     def Auto_caculate(self, r1, r2, axis):
#
#
#         if self.times_caculate < 5:  ####保存5测量结果
#             # self.result_tongkong[0] = ("%.2f" % (self.R1))
#             # self.result_tongkong[1] = ("%.2f" % (self.R2))
#             # self.result_tongkong[2] = ("%.2f" % (self.Axis))
#
#             self.show_hateman_rgb = cv2.cvtColor(self.show0, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
#             self.show_hateman = cv2.cvtColor(self.show_hateman_rgb, cv2.COLOR_RGB2GRAY)
#             ret2, self.img_jinshi_gray = cv2.threshold(self.show_hateman, self.num_jinshi, 255, cv2.THRESH_BINARY)
#             cv2.imwrite("./pic/jinshi_thresh_"+str(self.times_caculate)+".bmp", self.img_jinshi_gray)
#             cv2.imwrite("./pic/jinshi_gray_"+str(self.times_caculate)+".bmp", self.show_hateman)
#             quguangdu = self.caculate(self.img_jinshi_gray)  ####计算屈光度
#
#             self.R1[self.times_caculate] = r1    ####像素值
#             self.R2[self.times_caculate] = r2    ####像素值
#             self.Axis[self.times_caculate] = axis
#             self.SPH[self.times_caculate] = quguangdu[0]    ####SPH
#             self.CYL[self.times_caculate] = quguangdu[1]     ####CYL
#             self.A[self.times_caculate] = quguangdu[2]
#             self.times_caculate += 1
#
#         if self.times_caculate == 5:
#
#             SPH_mean = (self.SPH[0] + self.SPH[1] + self.SPH[2] + self.SPH[3] + self.SPH[4])/5
#             CYL_mean = (self.CYL[0] + self.CYL[1] + self.CYL[2] + self.CYL[3] + self.CYL[4])/5
#             A_mean = (self.A[0] + self.A[1] + self.A[2] + self.A[3] + self.A[4])/5
#             R1_mean = (self.R1[0] + self.R1[1] + self.R1[2] + self.R1[3] + self.R1[4]) / 5
#             R2_mean = (self.R2[0] + self.R2[1] + self.R2[2] + self.R2[3] + self.R2[4]) / 5
#             Axis_mean = (self.Axis[0] + self.Axis[1] + self.Axis[2] + self.Axis[3] + self.Axis[4])/5
#             self.final_result[0] = SPH_mean
#             self.final_result[1] = CYL_mean
#             self.final_result[2] = A_mean
#             self.final_result[3] = R1_mean/self.PIX_R1
#             self.final_result[4] = R2_mean/self.PIX_R2
#             self.final_result[5] = Axis_mean
#             np.savetxt("./tempfile_txt/final_result.txt", self.final_result, fmt='%2f')  ####保留两位小数
#             np.savetxt("./tempfile_txt/SPH_result.txt", self.SPH, fmt='%2f')  ####保留两位小数
#             np.savetxt("./tempfile_txt/CYL_result.txt", self.CYL, fmt='%2f')  ####保留两位小数
#             np.savetxt("./tempfile_txt/A_result.txt", self.A, fmt='%2f')  ####保留两位小数
#             np.savetxt("./tempfile_txt/R1_result.txt", self.R1, fmt='%2f')  ####保留两位小数
#             np.savetxt("./tempfile_txt/R2_result.txt", self.R2, fmt='%2f')  ####保留两位小数
#             np.savetxt("./tempfile_txt/Axis_result.txt", self.Axis, fmt='%2f')  ####保留两位小数
#             self.show_finalresult_L(self.final_result)
#
#             self.write_to_history_table(self.final_result)
#             # self.times_caculate = 0
#             # self.times_caculate += 1
#         ####保存瞳孔测试结果####
#
#         # np.savetxt("./tempfile_txt/result_tongkong.txt", self.result_tongkong, fmt='%s')
#         # ####保存屈光度测试结果####
#         # np.savetxt("./tempfile_txt/result_quguangdu.txt", self.result_quguangdu, fmt='%2f')  ####保留两位小数
#         ####显示左眼测试结果
#
#
#
#
#
#     # def update_pd(self, num):
#     #     self.sum_pd_move = self.sum_pd_move + num
#
#
#
# class Thread_Z_STEP(QThread):
#
#     def __init__(self,parent = None):
#         super().__init__(parent)
#
#
#     def run(self):
#
#
#          while True:
#             cpu_temp = self.get_cpu_temp()
#             time.sleep(0.5)
#
#
#             if bujindianji_Z.xainwei_zhedang():  ####限位开关没被遮挡
#                 try:
#                     global biase
#                     global mouse_move
#                     # biase_auto = np.loadtxt("./tempfile_txt/biase.txt")  ####获取圆环中心与屏幕中心偏差值
#                     biase_auto = biase
#                     step_auto = int(abs(biase_auto[1]) * 5.55)    ####5.55是像素值转为步进电机运转脉冲次数
#                     biase_mouse = mouse_move   ####当前鼠标位置-屏幕中心位置
#
#
#                     abs_move_y = int(abs(biase_mouse[1])*5.55)
#
#                     if biase_mouse[1] < 0:    ####鼠标点击上方，往上移动
#                         bujindianji_Z.backward(0.0001, abs_move_y)
#
#
#                     if biase_mouse[1] > 0:    ####鼠标点击下方，往下移动
#                         bujindianji_Z.forward(0.0001, abs_move_y)
#
#                     else:
#                         bujindianji_Z.stop()
#                     mouse_move = np.array([0, 0])   ####初始化
#
#
#
#
#
#
#
#
#                     # step = int(abs(biase[1])*5.55)
#                     if biase_auto[1] > 0 and 2 < abs(biase_auto[1]) < 200:  ####圆环中心在下面, 上下
#                         bujindianji_Z.forward(0.0001, int(step_auto / 2))
#
#                         bujindianji_Z.forward(0.0005, int(step_auto / 2))
#                         # global biase
#                         # biase_auto_update = np.array([0, 0, 0])
#                         # # np.savetxt("biase.txt", biase_auto_update, fmt='%s')
#                         # biase = biase_auto_update
#
#                     if biase_auto[1] < 0 and 2 < abs(biase_auto[1]) < 200:  ####圆环中心在上面
#
#                         bujindianji_Z.backward(0.0001, int(step_auto / 2))
#                         bujindianji_Z.backward(0.0005, int(step_auto / 2))
#                         # global biase
#                         # biase_auto_update = np.array([0, 0, 0])
#                         # # np.savetxt("biase.txt", biase_auto_update, fmt='%s')
#                         # biase = biase_auto_update
#
#
#
#
#                 except:
#                      bujindianji_Z.stop()
#
#             else:
#                  # msg = QtWidgets.QMessageBox.warning(self, 'warning', "步进电机已经到下限位，请抬高额托架",
#                  #                                    buttons=QtWidgets.QMessageBox.Ok)
#                  bujindianji_Z.backward(0.000000001, 2000)
#
#
#
#     def get_cpu_temp(self):
#         tempfile = open("/sys/class/thermal/thermal_zone0/temp")
#         cpu_temp = tempfile.read()
#         tempfile.close()
#         return float(cpu_temp)/1000
#
#     def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
#         if event == cv2.EVENT_LBUTTONDOWN:
#             xy = "%d,%d" % (x, y)
#             print(xy)
#
#
#
#
#
#
#
# class Thread_wuxiang_bujindianji(QThread):
#     def __init__(self,parent = None):
#         super().__init__(parent)
#         self.result_quguangdu = np.loadtxt("./tempfile_txt/result_quguangdu.txt")
#     def run(self):
#         self.lijiao = self.result_quguangdu[0]
#         step = abs(int(self.lijiao)) * 10
#         print(step)
#         if self.lijiao < 0:  #####近视物象补偿
#             bujindianji_wuxiang.forward(0.002, step)
#             time.sleep(0.001)
#             bujindianji_wuxiang.backward(0.002, step)
#             time.sleep(0.001)
#             bujindianji_wuxiang.stop()
#         if self.lijiao > 0:  #####远视物象补偿
#             bujindianji_wuxiang.backward(0.002, step)
#             time.sleep(0.001)
#             bujindianji_wuxiang.forward(0.002, step)
#             time.sleep(0.001)
#             bujindianji_wuxiang.stop()
#
# class Thread_tcp(QThread):
#     def __init__(self,parent = None):
#         super().__init__(parent)
#     def run(self):
#         tcp_server.socket_client()
#


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用
    win_custom = main_window()  ######主窗口
    # win_menu = menu_win()  #####用户菜单窗口
    # win_dev = dev_window()
    #
    # pixmap = QPixmap("./pic/ximinglogo.jpg")
    # screen = QSplashScreen(pixmap)
    #
    #
    #
    # screen.show()
    # # win_custom.caculate_zero()
    #
    # # dtimer = QElapsedTimer()
    # # delayTime = 5
    # # dtimer.start()
    # # while (dtimer.elapsed() < (delayTime * 1)):
    # #      {
    # #          app.processEvents()
    # #      }
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # win_menu.setWindowTitle("用户菜单")
    win_custom.setWindowTitle("希铭光学")
    # win_custom.autorun() ####程序启动时自动打开两个摄像头
    # ##########窗口在屏幕中央显示################33
    # desktop = QtWidgets.QApplication.desktop()
    # x = (desktop.width()-win_custom.width())//2
    # y = (desktop.height() - win_custom.height()) // 2
    # win_custom.move(x, y)
    # win_menu.move(x, y)
    win_custom.show()

    # win_custom.pushButton_set.clicked.connect(win_menu.show)
    # win_custom.pushButton_dev.clicked.connect(win_dev.show)
    # ################Z轴自动找眼######################
    #
    # thread_Z_STEP = Thread_Z_STEP()
    # thread_Z_STEP.start()
    # thread_TCP = Thread_tcp()
    # thread_TCP.start()

    # bujindianji_Z.backward(0.000000001, 4000)
    sys.exit(app.exec_())