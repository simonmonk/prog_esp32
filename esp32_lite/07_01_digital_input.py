from machine import Pin
from utime import sleep

switch = Pin(10, Pin.IN, Pin.PULL_UP)

while True:
    print(switch.value())
    sleep(0.1)