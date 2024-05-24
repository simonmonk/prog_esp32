from machine import DAC, Pin, Timer
from math import sin, radians

dac = DAC(Pin(25))

sine_table = []
num_samples = 36
angle_per_sample = 360 / num_samples
scale_factor = 100
offset = 127

def fill_sine_table():
    global sine_table
    for i in range(0, num_samples):
        angle_degrees = i * angle_per_sample
        sine_table.append(int(sin(radians(angle_degrees)) * scale_factor + offset))
        
i = 0        
        
def tick(timer):
    global i
    dac.write(sine_table[i])
    i += 1
    if i == num_samples:
        i = 0

fill_sine_table()
timer = Timer(0)

while True:
    f_str = input('Enter Frequency (Hz):')
    try:
        f = int(f_str)
        sample_f = f * num_samples
        timer.deinit()
        timer.init(freq=sample_f, mode=Timer.PERIODIC, callback=tick)
    except:
        print('bad frequency value')