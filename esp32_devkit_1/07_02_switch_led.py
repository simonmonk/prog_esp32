from machine import Pin, Signal
from time import sleep

switch = Pin(12, Pin.IN, Pin.PULL_UP)
led = Signal(22, Pin.OUT, invert=True)

while True:
    if switch.value() == 0:
        led.on()
        sleep(10)
        led.off()