from gpiozero import PWMLED
from time import sleep

yuanhuan_in = PWMLED(5)
yuanhuan_out = PWMLED(6)


def yuanhuandeng_on(value_in, value_out):
    yuanhuan_in.value = value_in
    yuanhuan_out.value = value_out


def yuanhuandeng_off():
    yuanhuan_in.value = 0
    yuanhuan_out.value = 0