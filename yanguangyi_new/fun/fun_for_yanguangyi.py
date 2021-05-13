
import numpy as np
import cv2 as cv




def caculate_center(img_gray):  ######计算质心

    hateman_v12_row = [21, 81, 148, 212, 278, 341, 409, 471]

    hateman_v12_col = [31, 86, 152, 220, 283, 352, 416, 483, 547, 611]

    s_sx_sy = np.zeros([37, 3])
    center = np.zeros([74, 1])
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


    try:

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
        for j in range(col4, col5):
            n = 4
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 5
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 6
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col7, col8):
            n = 7
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

       for i in range(row3, row4):  ####第三行7个
        for j in range(col2, col3):
            n = 8
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col3, col4):
            n = 9
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col4, col5):
            n = 10
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 11
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 12
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col7, col8):
            n = 13
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col8, col9):
            n = 14
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

       for i in range(row4, row5):  ####第四行7个
        for j in range(col2, col3):
            n = 15
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col3, col4):
            n = 16
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col4, col5):
            n = 17
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 18
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 19
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col7, col8):
            n = 20
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col8, col9):
            n = 21
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

       for i in range(row5, row6):  ####第五行7个
        for j in range(col2, col3):
            n = 22
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col3, col4):
            n = 23
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col4, col5):
            n = 24
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 25
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 26
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col7, col8):
            n = 27
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col8, col9):
            n = 28
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

       for i in range(row6, row7):  ####第六行5个
        for j in range(col3, col4):
            n = 29
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col4, col5):
            n = 30
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 31
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 32
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col7, col8):
            n = 33
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

       for i in range(row7, row8):  ####第七行3个
        for j in range(col4, col5):
            n = 34
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col5, col6):
            n = 35
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2
        for j in range(col6, col7):
            n = 36
            pix = img_gray[i, j]
            # p2 = pow(pix, 1)
            p2 = pow(pix, 2)
            s_sx_sy[n, 0] = s_sx_sy[n, 0] + p2
            s_sx_sy[n, 1] = s_sx_sy[n, 1] + j * p2
            s_sx_sy[n, 2] = s_sx_sy[n, 2] + i * p2

       for i in range(37):
          center[i, 0] = s_sx_sy[i, 1] / s_sx_sy[i, 0]
          center[i + 37, 0] = s_sx_sy[i, 2] / s_sx_sy[i, 0]
       return center
    except:
        print("质心计算错误")

# def bianlixiangsu():


def caculate_quguangdu(z3, z4, z5):
        r1 = 3.25
        r2 = r1 * r1
        num_jinshi = 1.15  ####近视补偿系数*
        num_yuanshi = 1.05  ####远视补偿系数/
        ###J45
        temp_1 = pow((z3 * z3 + z5 * z5), 0.5)
        th = np.arctan(z5 / z3)
        the_1 = np.degrees(th)

        cyl_1 = -4 * pow(6, 0.5) * temp_1 / r2
        if z4 < 0:

            if abs(cyl_1) < 1.5:
                sph_1 = 4 * pow(3, 0.5) * z4 / r2 - cyl_1 / 2


            else:
                sph_1 = 4 * pow(3, 0.5) * z4 / r2 - cyl_1 / 2
        if z4 > 0:

            if abs(cyl_1) < 1.5:
                sph_1 = 4 * pow(3, 0.5) * z4 / r2 + cyl_1 / 2


            else:
                sph_1 = 4 * pow(3, 0.5) * z4 / r2 + cyl_1 / 2

        if sph_1 > 0:
            sph_1 = sph_1 / num_yuanshi  #####"远视球镜度_2：",
        else:
            sph_1 = sph_1 * num_jinshi ####"近视球镜度_2：",
        if abs(cyl_1) < 0.5:
            cyl_1 = 0
            the_1 = 180  #####
        else:
            cyl_1 = cyl_1 ####"柱镜度_2：",
            if z3 < 0:
                the_1 = the_1 + 85  #####"轴位_2：%2f" %(
            if z3 > 0 and z5 < 0:
                the_1 = the_1 + 175
            if z3 > 0 and z5 > 0:
                the_1 = the_1
        result = [sph_1, cyl_1, the_1]
        return result


def verifySizes_big_circle(RotatedRect):
    error = 0.2

    aspect = 1

    min = 80 * aspect * 80   ####圆环最小直径

    max = 150 * aspect * 150   ####圆环最大直径

    rmin = aspect - aspect * error

    rmax = aspect + aspect * error

    height, width = RotatedRect[1]

    if height == 0 or width == 0:
        return False

    area = height * width

    r = width / height

    if r < 1:
        r = height / width

    if (area < min or area > max) or (r < rmin or r > rmax):

        return False

    else:

        return True


def verifySizes_small_circle(RotatedRect):
    error = 0.2

    aspect = 1

    min = 10 * aspect * 10   ####圆环最小直径

    max = 30 * aspect * 30   ####圆环最大直径

    rmin = aspect - aspect * error

    rmax = aspect + aspect * error

    height, width = RotatedRect[1]

    if height == 0 or width == 0:
        return False

    area = height * width

    r = width / height

    if r < 1:
        r = height / width

    if (area < min or area > max) or (r < rmin or r > rmax):

        return False

    else:

        return True


