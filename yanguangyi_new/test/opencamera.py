import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from gpiozero.pins.pigpio import PiGPIOFactory
import fun_for_yanguangyi   ####核心算法模块
import numpy as np
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
yuanhuan_x = 320
yuanhuan_y = 240
def opencarmera(win, index):
    timer_camera_tongkong = QtCore.QTimer()
    cap_tongkong = cv2.VideoCapture(index)
    flag = cap_tongkong.open(index)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频

    if flag == False:  # flag表示open()成不成功
        msg = QtWidgets.QMessageBox.warning(win, 'warning', "请检查哈特曼相机于电脑是否连接正确",
                                            buttons=QtWidgets.QMessageBox.Ok)
    else:
        timer_camera_tongkong.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示

    flag, image2 = cap_tongkong.read()  # 从视频流中读取
    show1 = cv2.resize(image2, (640, 480))  # 把读到的帧的大小重新设置为 640x480
    show2 = cv2.cvtColor(show1, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
    show3 = cv2.cvtColor(show2, cv2.COLOR_RGB2GRAY)
    show4 = cv2.GaussianBlur(show3, (5, 5), 1)
    cv2.circle(show2, (yuanhuan_x, yuanhuan_y), 100, (255, 0, 0), 2)
    cv2.line(show2, (yuanhuan_x - 20, yuanhuan_y), (yuanhuan_x + 20, yuanhuan_y), (255, 0, 0), 1)
    cv2.line(show2, (yuanhuan_x, yuanhuan_y - 20), (yuanhuan_x, yuanhuan_y + 20), (255, 0, 0), 1)
    ret, show5 = cv2.threshold(show4, 188, 255, cv2.THRESH_BINARY)
    show6 = cv2.Canny(show5, 40, 255)
    contours, hierarchy = cv2.findContours(show6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    save = []  # 存储合理轮廓

    rectall = []  # 存储对应的在最小面积矩形

    for contour in contours:

        rect = cv2.minAreaRect(contour)

        if fun_for_yanguangyi.verifySizes(rect):
            save.append(contour)

            rectall.append(rect)
    # cnt = contours[4]
    # print(len(save))
    for finalcontour in save:
        ellipse = cv2.fitEllipse(finalcontour)
        ellipse_center_x_biase = int(ellipse[0][0]) - yuanhuan_x
        ellipse_center_y_biase = int(ellipse[0][1]) - yuanhuan_y
        R1 = ellipse[1][0]
        R2 = ellipse[1][1]
        Axis = ellipse[2]
        # print(R1/21.5, R2/21.5, Axis)
        # text = "R1：%2d；R2：%2d；Axis：%2d" % (R1/21.5, R2/21.5, Axis)
        win.label_show_jiaomo.setText("R1：%.2f；\n"
                                             "R2：%.2f；\n"
                                             "Axis：%.2f" % (
                                             round(R1 / 21.5, 2), round(R2 / 21.5, 2),
                                             round(Axis, 2)))  #####换行显示
        if ellipse_center_x_biase in range(-10, 10) and ellipse_center_y_biase in range(-10, 10):
            cv2.circle(show2, (yuanhuan_x, yuanhuan_y), 100, (0, 255, 0), 2)
            cv2.line(show2, (yuanhuan_x - 20, yuanhuan_y), (yuanhuan_x + 20, yuanhuan_y),
                     (0, 255, 0), 1)
            cv2.line(show2, (yuanhuan_x, yuanhuan_y - 20), (yuanhuan_x, yuanhuan_y + 20),
                     (0, 255, 0), 1)
            # cv2.putText(show2, text, (70, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            cv2.drawContours(show2, save, -1, (0, 0, 255), 2)

    showImage = QtGui.QImage(show2.data, show2.shape[1], show2.shape[0],
                             QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
    win.label_show_pic.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
