from machine import Pin, PWM
from time import sleep

# UNTESTED SINCE PIN SWAP

red_ch = PWM(Pin(25))
green_ch = PWM(Pin(33))
blue_ch = PWM(Pin(32))

button = Pin(14, Pin.IN, Pin.PULL_UP)

colors = [[255, 0, 0], [127, 127, 0],[0, 255, 0], [0, 127, 127], [0, 0, 255], [127, 0, 127]]

def set_color(rgb):
    red_ch.duty_u16(rgb[0] * 256)
    green_ch.duty_u16(rgb[1] * 256)
    blue_ch.duty_u16(rgb[2] * 256)

index = 0
set_color(colors[index])
while True:
    if button.value() == 0:
        index +=1
        if index >= len(colors):
            index = 0
        sleep(0.2)
    set_color(colors[index])

