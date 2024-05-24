from machine import Pin, Signal
from time import sleep

led = Signal(22, Pin.OUT, invert=True)

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    blink(3, 0.2) # blink 3 times fast (S)
    sleep(0.4)
    blink(3, 0.6) # blink 3 times slow (O)
    sleep(0.4)