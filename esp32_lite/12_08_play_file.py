import time
from machine import DAC, Pin, Timer

filename = 'school_bell.raw'
dac = DAC(Pin(25))

buffer = []
num_samples = 0

def read_file():
    global buffer, num_samples
    try:
        f = open(filename, 'rb')
        buffer = f.read()
        num_samples = len(buffer)
        f.close()
    except:
        print("Couldn't find file: " + filename)
    
i = 0        
          
def tick(timer):
    global i
    dac.write(buffer[i])
    i += 1
    if i == num_samples:
        timer.deinit()

read_file()

timer = Timer(0)
timer.init(freq=8000, mode=Timer.PERIODIC, callback=tick)

while True:
    pass