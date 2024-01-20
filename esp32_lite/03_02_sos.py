from machine import Pin
from time import sleep

led = Pin(22, Pin.OUT)

while True:
    # S
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.6)
    # O
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)