from machine import Pin, Timer
from time import sleep

led = Pin(22, Pin.OUT)

led_state = 0

def tick(timer):
    global led, led_state
    led.value(led_state)
    led_state ^= 1 

timer = Timer(0)

timer.init(freq=2, mode=Timer.PERIODIC, callback=tick)

x = 0
while True:
    print(x)
    x += 1
    sleep(1.2)  