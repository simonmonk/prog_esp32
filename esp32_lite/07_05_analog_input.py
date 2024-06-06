from machine import ADC, Pin
from time import sleep

analog = ADC(32)

while True:
    reading = analog.read_u16()
    print(reading)
    sleep(0.5)