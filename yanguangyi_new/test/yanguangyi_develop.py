from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from test import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen, QInputDialog
from gpiozero import LED
from gpiozero import PWMLED, Button
import cv2 as cv
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import LEDBoard
import fun_for_yanguangyi   ####核心算法模块
import numpy as np
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QElapsedTimer, QObject, pyqtSignal
#######数据库所需
from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import xlrd                           #导入读取表格模块
from xlutils.copy import copy        #导入copy模块
import time
# import 数据库4  ####导入表格显示模块





class test_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 父类的构造函数
        self.setupUi(self)  # 初始化程序界面
        # factory = PiGPIOFactory(host='169.254.163.132')  # 填写树莓派的IP地址

        self.timer_camera_tongkong = QtCore.QTimer()
        self.timer_camera_hateman = QtCore.QTimer()# 定义定时器，用于控制显示视频的帧率

        self.cap_tongkong = cv2.VideoCapture()
        self.cap_hateman = cv2.VideoCapture()# 视频流
        self.CAM_TONGKONG = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.CAM_HATEMAN = 2
        ####验光仪光路硬件部分定义
        self.laser = PWMLED(17)
        self.wuxiang = PWMLED(6)
        self.yuanhuan_in = PWMLED(13)
        self.yuanhuan_out = PWMLED(16)
        self.buttun = Button(18)
        self.yuanhuan_in.value = 0.2
        self.laser.value = 0.25
        self.graph = LEDBoard(20, 21, 22, 23)

        #####圆环中心坐标
        self.yuanhuan_x = self.spinBox_up.value()
        self.yuanhuan_y = self.spinBox_right.value()
        self.slot_init()  # 初始化槽函数t自带的，会关闭程序
    def slot_init(self):

        ########瞳孔相机信号连接
        self.pushButton_opencamer.clicked.connect(
            self.button_open_camera_tongkong_clicked)  # 若该按键被点击，则调用button_open_camera_clicked()
        self.timer_camera_tongkong.timeout.connect(self.show_camera_tongkong)  # 若定时器结束，则调用show_camera()
        self.pushButton_closecamer.clicked.connect(self.close)  # 若该按键被点击，则调用close()，注意这个close是父类QtWidgets.QWidget自带的，会关闭程序


        ########hateman相机信号连接
        self.pushButton_capture_hateman.clicked.connect(
               self.button_open_camera_hateman_clicked)  # 若该按键被点击，则调用button_open_camera_clicked()
        self.timer_camera_hateman.timeout.connect(self.show_camera_hateman)  # 若定时器结束，则调用show_camera()

        #######切换相机信号连接
        self.pushButton_switch_to_tongkong.clicked.connect(
               self.button_switch_to_tongkong_clicked)
        self.pushButton_switch_to_hateman.clicked.connect(
               self.button_switch_to_hateman_clicked)
        #######屈光度测量按钮链接
        self.pushButton_caculate.clicked.connect(self.quguangdu)  ######计算屈光度
         ######光路硬件信号连接
        self.horizontalSlider_laser.valueChanged.connect(self.spinBox_laser.setValue)######滑轨与数字显示相连
        self.spinBox_laser.valueChanged.connect(self.horizontalSlider_laser.setValue)######滑轨与数字显示相连
        self.horizontalSlider_laser.valueChanged.connect(self.laser_control)

        self.horizontalSlider_wuxiang.valueChanged.connect(self.spinBox_wuxiang.setValue)  ######滑轨与数字显示相连
        self.spinBox_wuxiang.valueChanged.connect(self.horizontalSlider_wuxiang.setValue)  ######滑轨与数字显示相连
        self.horizontalSlider_wuxiang.valueChanged.connect(self.wuxiang_control)

        self.horizontalSlider_huanxingdeng_in.valueChanged.connect(self.spinBox_huanxingdeng_in.setValue)  ######滑轨与数字显示相连
        self.spinBox_huanxingdeng_in.valueChanged.connect(self.horizontalSlider_huanxingdeng_in.setValue)  ######滑轨与数字显示相连
        self.horizontalSlider_huanxingdeng_in.valueChanged.connect(self.yuanhuan_in_control)

        self.horizontalSlider_huanxingdeng_out.valueChanged.connect(
               self.spinBox_huanxingdeng_out.setValue)  ######滑轨与数字显示相连
        self.spinBox_huanxingdeng_out.valueChanged.connect(
               self.horizontalSlider_huanxingdeng_out.setValue)  ######滑轨与数字显示相连
        self.horizontalSlider_huanxingdeng_out.valueChanged.connect(self.yuanhuan_out_control)

       #####连接“输入姓名”信号
        self.pushButton_inputname.clicked.connect(self.inputname)

        #######连接圆环中心坐标值信号
        self.spinBox_up.valueChanged.connect(self.yuanhuan_x_change)
        self.spinBox_right.valueChanged.connect(self.yuanhuan_y_change)
        ######零位保存信号连接
        self.pushButton_zero.clicked.connect(self.save_zero_pic)


        self.pushButton_forward.clicked.connect(self.bujindianji_forward)
        self.pushButton_backward.clicked.connect(self.bujindianji_backward)

    def bujindianji_forward(self):
        for i in range(0, 20):
            self.graph.value = (1, 0, 0, 0)
            time.sleep(0.001)
            self.graph.value = (0, 1, 0, 0)
            time.sleep(0.001)
            self.graph.value = (0, 0, 1, 0)
            time.sleep(0.001)
            self.graph.value = (0, 0, 0, 1)
            time.sleep(0.001)

    def bujindianji_backward(self):
        for i in range(0, 20):
            self.graph.value = (0, 0, 0, 1)
            time.sleep(0.001)
            self.graph.value = (0, 0, 1, 0)
            time.sleep(0.001)
            self.graph.value = (0, 1, 0, 0)
            time.sleep(0.001)
            self.graph.value = (1, 0, 0, 0)
            time.sleep(0.001)

    def laser_control(self, laser_lightness):
        self.laser.value = laser_lightness/100
    def wuxiang_control(self, wuxiang_lightness):
        self.wuxiang.value = wuxiang_lightness/100
    def yuanhuan_in_control(self, yuanhuan_in_lightness):
        self.yuanhuan_in.value = yuanhuan_in_lightness/100
    def yuanhuan_out_control(self, yuanhuan_out_lightness):
        self.yuanhuan_out.value = yuanhuan_out_lightness/100
    def yuanhuan_x_change(self):
        self.yuanhuan_x = self.spinBox_up.value()

    def yuanhuan_y_change(self):
        self.yuanhuan_y = self.spinBox_right.value()

    def inputname(self):
        self.text, self.ok = QInputDialog.getText(self, 'Input Dialog',
                                                  'Enter file name:')
    def button_open_camera_hateman_clicked(self):

        self.label_show_hateman_video.show()
        self.label_show_tongkong_video.hide()

        if self.timer_camera_hateman.isActive() == False:  # 若定时器未启动
            flag = self.cap_hateman.open(self.CAM_HATEMAN)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频

            if flag == False:  # flag表示open()成不成功
               msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查哈特曼相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
               self.timer_camera_hateman.start(60)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示


               self.pushButton_capture_hateman.setText('(关闭)hateman相机')
        else:
            self.timer_camera_hateman.stop()  # 关闭定时器
            self.cap_hateman.release()  # 释放视频流
            self.label_show_hateman_video.clear()  # 清空视频显示区域
            self.pushButton_capture_hateman.setText('打开hateman相机')
    def show_camera_hateman(self):

        flag, self.image = self.cap_hateman.read()  # 从视频流中读取
        self.show0 = cv2.resize(self.image, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        self.show_hateman = cv2.cvtColor(self.show0, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色

        file_savepath_jinshi = str(self.text) + ".bmp"

        if self.buttun.is_active:
            self.quguangdu()
            cv2.imwrite(file_savepath_jinshi, self.show)

        showImage = QtGui.QImage(self.show_hateman.data, self.show_hateman.shape[1], self.show_hateman.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.label_show_hateman_video.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

    def button_switch_to_tongkong_clicked(self):
        self.label_show_hateman_video.hide()
        self.label_show_tongkong_video.show()

    def button_switch_to_hateman_clicked(self):
        self.label_show_hateman_video.show()
        self.label_show_tongkong_video.hide()

    def save_zero_pic(self):
        num_zero = 150  ####零位二值化阈值
        cv.imwrite("0.bmp", self.show_hateman)
        time.sleep(0.025)
        file_savepath_zero = str(0) + ".bmp"
        img_zero = cv.imread(file_savepath_zero, 0)
        ret1, img_zero_gray = cv.threshold(img_zero, num_zero, 255, cv.THRESH_BINARY)
        cv.imshow("zero", img_zero_gray)
        cv.waitKey()
        zero_center = fun_for_yanguangyi.caculate_center(img_zero_gray)
        np.savetxt("zero_center.txt", zero_center)
    def quguangdu(self):
        num = 0.0045  #####实际质心位置与质心像素坐标转换系数

        num_zero = 180
        num_jishi = 180  ####近视二值化阈值
        # self.text1, ok = QInputDialog.getText(self, 'Input Dialog',
        #                                 'Enter file name:')
        #
        # if ok:

        print(self.text)

        file_savepath_jinshi = self.text+".bmp"

        cv2.imwrite(file_savepath_jinshi, self.show_hateman)


        img_zero = cv.imread("0.bmp", 0)
        img_jinshi = cv.imread(file_savepath_jinshi, 0)
        ret, img_zero_gray = cv.threshold(img_zero, num_zero, 255, cv.THRESH_TOZERO)
        ret2, img_jinshi_gray = cv.threshold(img_jinshi, num_jishi, 255, cv.THRESH_TOZERO)
        cv.imshow("0", img_zero_gray)
        cv.imshow("jinshi", img_jinshi_gray)
        cv.waitKey(0)
        zernike = np.loadtxt("zernike_r_l_1_3_25.txt",
                                 dtype=np.float32)
        zero_center = fun_for_yanguangyi.caculate_center(img_zero_gray)  ####计算零位质心
        jinshi_center = fun_for_yanguangyi.caculate_center(img_jinshi_gray)  ####计算近视质心
        wavefront_slop = num * (zero_center - jinshi_center)
        print(wavefront_slop)
        zernike_cofficient = np.matmul(zernike, wavefront_slop)
        z3 = 1000 * zernike_cofficient[2, 0]  ####J0
        z4 = 1000 * zernike_cofficient[3, 0]
        z5 = 1000 * zernike_cofficient[4, 0]
        result = fun_for_yanguangyi.caculate_quguangdu(z3, z4, z5)
        #####将结果写入excel表
        # self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # ####写入excel表格
        # self.rb = xlrd.open_workbook('ximing.xls')  # 打开希铭.xls文件
        # self.wb = copy(self.rb)  # 利用xlutils.copy下的copy函数复制
        # self.sheet = self.rb.sheets()[0]  # 获取当前sheet
        # self.ws = self.wb.get_sheet(0)  ###获取修改当前sheet
        # self.current_rows = self.sheet.nrows  # 获取当前行数
        # self.ws.write(self.current_rows, 0, self.text)####第一列：姓名
        # self.ws.write(self.current_rows, 1, round(result[0], 2))####第二例：球镜度数
        # self.ws.write(self.current_rows, 2, round(result[1], 2))####第三列：柱镜度数
        # self.ws.write(self.current_rows, 3, round(result[2], 2))####第四例：轴位
        # self.ws.write(self.current_rows, 4, round(self.R1/21.5, 2))  ####第5列：R1
        # self.ws.write(self.current_rows, 5, round(self.R2/21.5, 2))  ####第6列：R2
        # self.ws.write(self.current_rows, 6, round(self.Axis, 2))  ####第7列：角膜轴位
        # self.ws.write(self.current_rows, 7, self.time)  ####第7列：角膜轴位
        # self.wb.save("ximing.xls")
        self.label_showresult.setText("S：%.2f；\n"
                               "C：%.2f；\n"
                               "A：%.2f" % (result[0], result[1], result[2]))  #####换行显示
    def button_open_camera_tongkong_clicked(self):
        self.label_show_hateman_video.hide()
        self.label_show_tongkong_video.show()
        if self.timer_camera_tongkong.isActive() == False:  # 若定时器未启动
            flag = self.cap_tongkong.open(self.CAM_TONGKONG)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查瞳孔相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera_tongkong.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                self.pushButton_opencamer.setText('（关闭）瞳孔相机')
        else:
            self.timer_camera_tongkong.stop()  # 关闭定时器
            self.cap_tongkong.release()  # 释放视频流
            self.label_show_tongkong_video.clear()  # 清空视频显示区域
            self.pushButton_opencame.setText('打开瞳孔相机')



    def show_camera_tongkong(self):

        flag, self.image2 = self.cap_tongkong.read()  # 从视频流中读取

        show1 = cv2.resize(self.image2, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        show2 = cv2.cvtColor(show1, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
        show3 = cv2.cvtColor(show2, cv2.COLOR_RGB2GRAY)
        show4 = cv2.GaussianBlur(show3, (5, 5), 1)
        cv2.circle(show2, (self.yuanhuan_x, self.yuanhuan_y), 100, (255, 0, 0), 2)
        cv2.line(show2, (self.yuanhuan_x-20, self.yuanhuan_y), (self.yuanhuan_x+20, self.yuanhuan_y), (255, 0, 0), 1)
        cv2.line(show2, (self.yuanhuan_x, self.yuanhuan_y-20), (self.yuanhuan_x, self.yuanhuan_y+20), (255, 0, 0), 1)
        ret, show5 = cv2.threshold(show4, 188, 255, cv2.THRESH_BINARY)
        show6 = cv2.Canny(show5, 40, 255)
        contours, hierarchy = cv.findContours(show6, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        save = []  # 存储合理轮廓

        rectall = []  # 存储对应的在最小面积矩形

        for contour in contours:

            rect = cv.minAreaRect(contour)

            if fun_for_yanguangyi.verifySizes(rect):
                save.append(contour)

                rectall.append(rect)
        # cnt = contours[4]
        # print(len(save))
        for finalcontour in save:
            ellipse = cv.fitEllipse(finalcontour)
            ellipse_center_x_biase = int(ellipse[0][0]) - self.yuanhuan_x
            ellipse_center_y_biase = int(ellipse[0][1]) - self.yuanhuan_y
            self.R1 = ellipse[1][0]
            self.R2 = ellipse[1][1]
            self.Axis = ellipse[2]
            # print(R1/21.5, R2/21.5, Axis)
            # text = "R1：%2d；R2：%2d；Axis：%2d" % (R1/21.5, R2/21.5, Axis)
            self.label_show_jiaomo.setText("R1：%.2f；\n"
                                      "R2：%.2f；\n"
                                      "Axis：%.2f" % (round(self.R1/21.5, 2), round(self.R2/21.5,2) ,round(self.Axis,2)))  #####换行显示
            if ellipse_center_x_biase in range(-10, 10) and ellipse_center_y_biase in range(-10, 10):
                cv2.circle(show2, (self.yuanhuan_x, self.yuanhuan_y), 100, (0, 255, 0), 2)
                cv2.line(show2, (self.yuanhuan_x - 20, self.yuanhuan_y), (self.yuanhuan_x + 20, self.yuanhuan_y),
                         (0, 255, 0), 1)
                cv2.line(show2, (self.yuanhuan_x, self.yuanhuan_y - 20), (self.yuanhuan_x, self.yuanhuan_y + 20),
                         (0, 255, 0), 1)
                # cv2.putText(show2, text, (70, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                cv.drawContours(show2, save, -1, (0, 0, 255), 2)



        showImage = QtGui.QImage(show2.data, show2.shape[1], show2.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.label_show_tongkong_video.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序应用

    pixmap = QPixmap("ximinglogo.jpg")
    screen = QSplashScreen(pixmap)



    screen.show()
    dtimer = QElapsedTimer()
    delayTime = 5
    dtimer.start()
    while (dtimer.elapsed() < (delayTime * 100)):
         {
             app.processEvents()
         }

    T = test_window()
    # H = 数据库4.Ui_MainWindow()
    T.setWindowTitle("希铭光学")
    T.show()
    # T.pushButton_history.clicked.connect(H.show)

    sys.exit(app.exec_())