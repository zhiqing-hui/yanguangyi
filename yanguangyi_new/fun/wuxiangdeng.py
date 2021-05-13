from gpiozero import PWMLED

wuxiangdeng = PWMLED(11)


def wuxiangdeng_on(lightvalue):
    wuxiangdeng.value = lightvalue


def wuxiangdeng_off():
    wuxiangdeng.value = 0