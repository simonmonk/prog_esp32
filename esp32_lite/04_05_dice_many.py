from machine import Pin, Signal
from time import sleep
from random import randint

led = Signal(22, Pin.OUT, invert=True)

def throw_dice(num_dice=1):
    total = 0
    for x in range(1, num_dice+1):
        total += randint(1, 6)
    return total

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    input()
    dice_throw = throw_dice(num_dice=2)
    print(dice_throw)
    blink(dice_throw, 0.2)
    