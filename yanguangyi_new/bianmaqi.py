#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RoAPin = 17  # CLK Pin
RoBPin = 18  # DT Pin
BtnPin = 27  # Button Pin

globalCounter = 0

flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0


def setup():
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(RoAPin, GPIO.IN)  # input mode
    GPIO. setup(RoBPin, GPIO.IN)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter
    Last_RoB_Status = GPIO.input(RoBPin)
    while (not GPIO.input(RoAPin)):  # 未旋转时，GPIO.input(RoAPin)值为1，旋转时会变为0
        Current_RoB_Status = GPIO.input(RoBPin)  # 旋转时的当前值
        flag = 1
    if flag == 1:
        flag = 0
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter = globalCounter + 1  # 顺时针旋转，角位移增大
        if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter = globalCounter - 1  # 逆时针旋转，数值减小


def btnISR(channel):
    global globalCounter
    globalCounter = 0


def loop():
    global globalCounter
    tmp = 0  # Rotary Temperary

    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=btnISR)
    # 当按下按钮时，调用回调函数btnISR
    while True:
        rotaryDeal()
        if tmp != globalCounter:
            print('globalCounter = %d' % globalCounter)
            tmp = globalCounter


def destroy():
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
