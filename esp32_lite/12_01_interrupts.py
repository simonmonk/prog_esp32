from machine import Pin
from time import sleep

button = Pin(14, Pin.IN, Pin.PULL_UP)

def handle_button(ignore):
    print('BUTTON PRESSED')

button.irq(handle_button, Pin.IRQ_RISING)

i = 0

while True:
    i += 1
    print(i)
    sleep(0.2)
