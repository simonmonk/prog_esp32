from machine import Pin, Signal
from time import sleep

led = Signal(22, Pin.OUT, invert=True)
delays = [0.2, 0.2, 0.2, 0.6, 0.6, 0.6]

while True:
    for delay in delays:
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        