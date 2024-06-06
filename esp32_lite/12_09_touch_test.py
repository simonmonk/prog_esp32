from machine import TouchPad, Pin
from time import sleep

touch_pad = TouchPad(Pin(32))

while True:
    print(touch_pad.read())
    sleep(0.5)