from machine import Pin
from time import sleep

led = Pin(22, Pin.OUT)
delays = [0.2, 0.2, 0.2, 0.6, 0.6, 0.6]

while True:
    for delay in delays:
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        