from gpiozero import PWMLED

DCM_1 = PWMLED(9)
DCM_2 = PWMLED(10)


def yunguangdianji_on():
    DCM_1.value = 1
    DCM_2.value = 0


def yunguangdianji_off():
    DCM_1.value = 0
    DCM_2.value = 0