from machine import Pin, Signal
from time import sleep
from random import randint

led = Signal(22, Pin.OUT, invert=True)

def throw_dice():
    return randint(1, 6)

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)
        
while True:
    # Wait for Enter to be pressed
    input('Press Enter in Shell to Throw Dice')
    # Enter has been pressed
    dice_throw = throw_dice()
    print(dice_throw)
    blink(dice_throw, 0.2)
