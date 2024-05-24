from machine import Signal, Pin
from time import sleep

led = Signal(22, Pin.OUT, invert=True)

while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
    