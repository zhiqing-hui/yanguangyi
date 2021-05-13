
from gpiozero import PWMLED
from time import sleep

laser = PWMLED(13)


def laser_on(lightvalue):
    laser.value = lightvalue



def laser_off():
    laser.value = 0