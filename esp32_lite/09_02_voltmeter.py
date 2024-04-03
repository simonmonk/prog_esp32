from machine import ADC, Pin
from time import sleep

analog = ADC(Pin(32), atten=ADC.ATTN_11DB)

while True:
    reading = analog.read_uv() / 1000000
    print(reading)
    sleep(0.5)