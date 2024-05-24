from machine import Pin, Signal
from time import sleep

switch = Pin(15, Pin.IN, Pin.PULL_UP)
led = Signal(2, Pin.OUT)

while True:
    if switch.value() == 0:
        led.on()
        sleep(10)
        led.off()