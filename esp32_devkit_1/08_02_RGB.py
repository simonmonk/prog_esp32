from machine import Pin, PWM
from time import sleep

red_ch = PWM(Pin(25))
green_ch = PWM(Pin(33))
blue_ch = PWM(Pin(32))

colors = [
    [255, 0, 0],   # red
    [127, 127, 0], # orange
    [0, 255, 0],   # green
    [0, 127, 127], # cyan
    [0, 0, 255],   # blue
    [127, 0, 127]  # purple
]

def set_color(rgb):
    red_ch.duty_u16(rgb[0] * 256) # 16 bit from 8 bit
    green_ch.duty_u16(rgb[1] * 256)
    blue_ch.duty_u16(rgb[2] * 256)

index = 0
set_color(colors[index])
while True:
    index +=1
    if index >= len(colors):
        index = 0
    sleep(0.2)
    set_color(colors[index])
