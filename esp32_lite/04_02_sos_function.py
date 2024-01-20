from machine import Pin
from time import sleep

led = Pin(22, Pin.OUT)

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    blink(3, 0.2)
    sleep(0.4)
    blink(3, 0.6)