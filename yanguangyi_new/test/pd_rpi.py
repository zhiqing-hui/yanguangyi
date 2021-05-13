#!/usr/bin/env python
import RPi.GPIO as GPIO

PIPin = 16
Rpin = 12
Gpin = 13


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(Gpin, GPIO.OUT)  # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT)  # Set Red Led Pin mode to output
    GPIO.setup(PIPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.add_event_detect(PIPin, GPIO.BOTH, callback=detect, bouncetime=200)


def Led(x):  # 控制双色LED灯闪烁的函数
    if x == 0:  # 没有遮挡光线，电路联通，传感器输出低电平，红灯亮
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    if x == 1:  # 光线被遮挡，电路断开，传感器输出高电平，绿灯亮
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)


def Print(x):  # 打印光线被遮挡提示消息
    if x == 1:
        print("    *************************")
        print('    *   Light was blocked   *')
        print('    *************************')


def detect(chn):
    Led(GPIO.input(PIPin))  # 控制双色LED灯闪烁的函数
    Print(GPIO.input(PIPin))  # 打印光线被遮挡提示消息


def loop():
    while True:
        pass  # pass语句就是空语句


def destroy():
    GPIO.output(Gpin, GPIO.LOW)  # Green led off
    GPIO.output(Rpin, GPIO.LOW)  # Red led off
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
