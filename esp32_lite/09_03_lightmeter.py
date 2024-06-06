from machine import ADC, Pin
from time import sleep

analog = ADC(Pin(32), atten=ADC.ATTN_11DB)

max_reading = 58000

while True:
    reading = analog.read_u16()
    percent = int(reading / max_reading * 100)
    if percent > 100:
        percent = 100
    print(percent)
    sleep(0.5)