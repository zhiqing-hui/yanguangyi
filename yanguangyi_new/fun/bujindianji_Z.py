from gpiozero import LEDBoard, LED, Button, PWMLED
from time import sleep
import threading


graph = LEDBoard(12, 7, 23, 24)

enable = LED(19)  ####使能开关
enable.value = 1
xianwei_switch = Button(8)


def stop():
    graph.value = (0, 0, 0, 0)







def forward(delay, steps):
    for i in range(0, steps):
        graph.value = (0, 1, 0, 1)
        sleep(delay)
        graph.value = (0, 1, 1, 0)
        sleep(delay)
        graph.value = (1, 1, 0, 0)
        sleep(delay)
        graph.value = (1, 1, 0, 0)
        sleep(delay)


def backward(delay, steps):
    for i in range(0, steps):
        graph.value = (1, 0, 0, 1)
        sleep(delay)
        graph.value = (1, 0, 0, 1)
        sleep(delay)
        graph.value = (0, 0, 1, 0)
        sleep(delay)
        graph.value = (1, 0, 1, 0)
        sleep(delay)


def loop():
    while True:

        print("forward...")

        forward(0.0000001, 1000)  # down

        print("stop...")
        stop()  # stop
        sleep(1)  # sleep 3s

        print("backward...")
        backward(0.000000001, 1000)  # up

        print("stop...")
        stop()
        sleep(1)
    else:
        self.stop()


def xainwei_zhedang():
    if xianwei_switch.is_active:  ####步进电机限位开关，默认不遮挡
        return True
    else:
        return False