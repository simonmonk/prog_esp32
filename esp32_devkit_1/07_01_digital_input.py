from machine import Pin
from time import sleep

switch = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    print(switch.value())
    sleep(0.1)
