from gpiozero import LEDBoard, LED, Button, PWMLED
from time import sleep

graph = LEDBoard(2, 3, 4, 17)
led = LED(22)  ####12v
led.value = 1


def stop():
    graph.value = (0, 0, 0, 0)


def forward(delay, steps):
    for i in range(0, steps):
        graph.value = (1, 0, 0, 0)
        sleep(delay)
        graph.value = (0, 1, 0, 0)
        sleep(delay)
        graph.value = (0, 0, 1, 0)
        sleep(delay)
        graph.value = (0, 0, 0, 1)
        sleep(delay)


def backward(delay, steps):
    for i in range(0, steps):
        graph.value = (0, 0, 0, 1)
        sleep(delay)
        graph.value = (0, 0, 1, 0)
        sleep(delay)
        graph.value = (0, 1, 0, 0)
        sleep(delay)
        graph.value = (1, 0, 0, 0)
        sleep(delay)