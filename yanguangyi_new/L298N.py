# 树莓派通过PCF8574来控制L298N控制的例子, 包括PWM调速功能
# 属于智能语音控制树莓派小车的车辆控制部分

# 连接方式:
#  ENDx口直接连树莓派GPIO
#  INx口 连接PCF8574的pin口, 然后PCF8574通过I2C连接到树莓派I2C接口

# 控制方式:
#  1. 针对ENDx口的PWM调速,直接通过GPIO口下发.
#  2. 针对INx口的电机转向控制, 通过PCF8574下发.
#  以上两种方式的控制,都通过general_io库封装对调用者不可见, 使用统一G_IO接口:
#     general_io库会自动识别,若端口是"I2"、'I7'这种类型,则使用i2c方式设置端口,
#     否则使用GPIO方式


# 端口标识: 其中I0,I2这种表示通过PCF8574连接到树莓派; 20,16这种方式表示直连GPIO

'''
use two L298N to control 4 engine
CTRL 1：
          ENDA   1    2    3    4    ENDB
          黄     橙   红  棕   黑    白
BCM:  P21    I0   I1  I2   I3    P20

CTRL 2：
          ENDA 1    2    3    4    ENDB
          黑   白   灰   紫   蓝   绿
BCM:  P12  I7   I6   I5   I4   P16

'''

import RPi.GPIO as GPIO  # 使用GPIO常量, 例如GPIO.HIGH
from fun.general_io import G_IO  # I2C接口和GPIO接口 统一调用库
# from log import debug, log  # 日志
import time
gio = G_IO(GPIO_mode=GPIO.BCM, i2c_index=1, i2c_addr=0x20)
gio.setup('I1', GPIO.OUT)
while True:

   gio.output('I1', 1)
# CTRL1 = {'ENDA': 21, 'IN1': 'I0', 'IN2': 'I1', 'IN3': 'I2', 'IN4': 'I3', 'ENDB': 20}
# CTRL2 = {'ENDA': 12, 'IN1': 'I7', 'IN2': 'I6', 'IN3': 'I5', 'IN4': 'I4', 'ENDB': 16}
#
#
# class Moto_Ctrl:
#     def __init__(self):
#         #
#         # GPIO_mode: GPIO.BCM or GPIO.BOARD, 若用到GPIO端口需设置
#         # i2c_index: 树莓派3一般是1, 表示chip. i2cdetect -l查到
#         # i2c_addr: i2c 设备的地址, 例如0x20, 此处为PCF8574的I2C地址.
#         #           可使用i2cdetect -1 查到(其中1代表i2c_index的值)
#         self.gio = G_IO(GPIO_mode=GPIO.BCM, i2c_index=1, i2c_addr=0x20)
#         for key in CTRL1:
#             port = CTRL1[key]
#             # debug("Moto_Ctrl::__init__(): set GPIO.OUT for port %s" % port )
#             self.gio.setup(port, GPIO.OUT)
#
#         for key in CTRL2:
#             port = CTRL2[key]
#             # debug("Moto_Ctrl::__init__(): set GPIO.OUT for port %s" % port )
#             self.gio.setup(port, GPIO.OUT)
#
#         # make all output port LOW
#         self.stop()
#
#         # setup the pwm for speed controller
#         self.pwms = []
#         # four control channels from two L198N controller
#         channels = [CTRL1["ENDA"], CTRL1["ENDB"], CTRL2["ENDA"], CTRL2["ENDB"]]
#         for channel in channels:
#             # debug("Moto_Ctrl::__init__(): set pwm for channel %s" % channel)
#             # the frequency is set to 150HZ
#             p = GPIO.PWM(channel, 150)
#             # the duty cycle is init to zero
#             p.start(0)
#             self.pwms.append(p)
#
#     def __del__(self):
#         self.pwms = []
#         self.gio = None
#
#     # set the speed
#     # duty_cycle:  [0,100]
#     def set_speed(self, duty_cycle):
#         # set the speed using the duty_cycle
#         for p in self.pwms:
#             # debug("Moto_Ctrl::set_speed(): set ducy cycle for channel %s" % p)
#             p.ChangeDutyCycle(duty_cycle)
#
#     #  stop
#     def stop(self):
#         for key in CTRL1:
#             if key.startswith("IN"):
#                 port = CTRL1[key]
#                 # debug("Moto_Ctrl::stop(): set GPIO.LOW  port %s" % port )
#                 self.gio.output(port, GPIO.LOW)
#
#         for key in CTRL2:
#             if key.startswith("IN"):
#                 port = CTRL2[key]
#                 # debug("Moto_Ctrl::stop(): set GPIO.LOW  port %s" % port )
#                 self.gio.output(port, GPIO.LOW)
#
#     def left_forward(self):
#         # left rear wheels
#         self.gio.output(CTRL2["IN3"], GPIO.LOW)
#         self.gio.output(CTRL2["IN4"], GPIO.HIGH)
#         # lefe front wheels
#         self.gio.output(CTRL2["IN1"], GPIO.HIGH)
#         self.gio.output(CTRL2["IN2"], GPIO.LOW)
#
#     def rigth_forward(self):
#         # right rear wheels
#         self.gio.output(CTRL1["IN1"], GPIO.HIGH)
#         self.gio.output(CTRL1["IN2"], GPIO.LOW)
#         # right front wheels
#         self.gio.output(CTRL1["IN3"], GPIO.HIGH)
#         self.gio.output(CTRL1["IN4"], GPIO.LOW)
#
#     def right_backward(self):
#         # right rear wheels
#         self.gio.output(CTRL1["IN1"], GPIO.LOW)
#         self.gio.output(CTRL1["IN2"], GPIO.HIGH)
#         # right front wheels
#         self.gio.output(CTRL1["IN3"], GPIO.LOW)
#         self.gio.output(CTRL1["IN4"], GPIO.HIGH)
#
#     def left_backward(self):
#         # left rear wheels
#         self.gio.output(CTRL2["IN3"], GPIO.HIGH)
#         self.gio.output(CTRL2["IN4"], GPIO.LOW)
#         # lefe front wheels
#         self.gio.output(CTRL2["IN1"], GPIO.LOW)
#         self.gio.output(CTRL2["IN2"], GPIO.HIGH)
#
#     # 控制小车行为,对外暴露接口
#     # action: string, 'forward','backwoard','turnleft','turnright'
#     #         'back_turnright', 'back_turnleft', 'stop'
#     # speed: int, range [0,100]
#     # duration: 持续时间, 若不传入, 则持续时间由外部控制
#     def control(self, action, speed, duration=None):
#         self.set_speed(speed)
#         if action == 'forward':
#             # debug("Moto_Ctrl::control(): forward")
#             self.left_forward()
#             self.rigth_forward()
#         elif action == 'backward':
#             # debug("Moto_Ctrl::control(): backward")
#             self.right_backward()
#             self.left_backward()
#         elif action == 'turnleft':
#             # debug("Moto_Ctrl::control(): turn left")
#             self.stop()
#             self.rigth_forward()
#         elif action == 'turnright':
#             # debug("Moto_Ctrl::control(): turn right")
#             self.stop()
#             self.left_forward()
#         elif action == 'back_turnright':
#             # debug("Moto_Ctrl::control(): back turn right")
#             self.stop()
#             self.left_backward()
#         elif action == 'back_turnleft':
#             # debug("Moto_Ctrl::control(): back turn left")
#             self.stop()
#             self.right_backward()
#         elif action == 'stop':
#             # debug("Moto_Ctrl::control(): turn right")
#             self.stop()
#         if duration != None:
#             time.sleep(duration)
#
#
# if __name__ == '__main__':
#     ctrl = Moto_Ctrl()
#     ctrl.control('backward', 90, 3)
#
#     ctrl.control('turnright', 60, 3)
#
#     ctrl.control('turnleft', 60, 3)
#
#     ctrl.control('forward', 60, 3)
#
#     ctrl.control('back_turnleft', 60, 3)
#
#     ctrl.control('back_turnright', 60, 3)
#
#     GPIO.cleanup()