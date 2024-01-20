from machine import Pin
from time import sleep

led = Pin(22, Pin.OUT)

while True:
    led.on()
    sleep(0.5) # pause
    led.off()
    sleep(0.5)
    