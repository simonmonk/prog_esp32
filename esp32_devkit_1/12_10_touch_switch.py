from machine import TouchPad, Pin, Signal
from time import sleep

touch_pad = TouchPad(Pin(32))
led = Signal(22, Pin.OUT, invert=True)

touch_thresold = 100

while True:
    if touch_pad.read() < touch_thresold:
        led.on()
    else:
        led.off()