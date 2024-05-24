from machine import ADC, Pin
from time import sleep

analog = ADC(Pin(32), atten=ADC.ATTN_11DB)

mv_per_c = 10
mv_offset = 500

while True:
    mv = analog.read_uv() / 1000
    temp_c = (mv - mv_offset) / mv_per_c
    print(temp_c)
    sleep(0.5)