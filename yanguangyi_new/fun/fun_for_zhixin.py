import numpy as np
import cv2 as cv
from numba import jit


@jit
def caculate_center(img_gray):  ######计算质心

    hateman_v12_row = [21, 81, 148, 212, 278, 341, 409, 471]

    hateman_v12_col = [31, 86, 152, 220, 283, 352, 416, 483, 547, 611]

    s_sx_sy = np.zeros([16, 3], dtype=np.float32)
    center = np.zeros([16, 2], dtype=np.float32)
    row1 = hateman_v12_row[0]
    row2 = hateman_v12_row[1]
    row3 = hateman_v12_row[2]
    row4 = hateman_v12_row[3]
    row5 = hateman_v12_row[4]
    row6 = hateman_v12_row[5]
    row7 = hateman_v12_row[6]
    row8 = hateman_v12_row[7]

    col2 = hateman_v12_col[1]
    col3 = hateman_v12_col[2]
    col4 = hateman_v12_col[3]
    col5 = hateman_v12_col[4]
    col6 = hateman_v12_col[5]
    col7 = hateman_v12_col[6]
    col8 = hateman_v12_col[7]
    col9 = hateman_v12_col[8]
    # try:

    for i in range(row1, row2):
        for j in range(col4, col5):
            n = 0
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 1
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 2
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

    for i in range(row2, row3):
        for j in range(col3, col4):
            n = 3
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

        for j in range(col7, col8):
            n = 4
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

    for i in range(row3, row4):  ####第三行2个
        for j in range(col2, col3):
            n = 5
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

        for j in range(col8, col9):
            n = 6
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

    for i in range(row4, row5):  ####第四行2个
        for j in range(col2, col3):
            n = 7
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

        for j in range(col8, col9):
            n = 8
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

    for i in range(row5, row6):  ####第五行2个
        for j in range(col2, col3):
            n = 9
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

        for j in range(col8, col9):
            n = 10
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

    for i in range(row6, row7):  ####第六行2个
        for j in range(col3, col4):
            n = 11
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

        for j in range(col7, col8):
            n = 12
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

    for i in range(row7, row8):  ####第七行3个
        for j in range(col4, col5):
            n = 13
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 14
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 15
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

    for i in range(16):
        center[i, 0] = s_sx_sy[i, 1] / s_sx_sy[i, 0]
        center[i, 1] = s_sx_sy[i, 2] / s_sx_sy[i, 0]
    ellipse = cv.fitEllipse(center)
    return ellipse
