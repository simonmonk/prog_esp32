from machine import Pin
from time import sleep

led = Pin(32, Pin.OUT)

while True:
    led.value(1)
    sleep(0.5) # pause
    led.value(0)
    sleep(0.5)
    
