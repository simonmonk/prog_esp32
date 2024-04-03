from network import WLAN, STA_IF
from microdot import Microdot
from machine import ADC, Pin
from time import sleep

ssid = 'network'
password = 'password'

max_reading = 58000

sensor = ADC(Pin(32), atten=ADC.ATTN_11DB)

def connect_wifi(ssid, password):
    wlan = WLAN(STA_IF)
    wlan.active(True)
    print('connecting to ' + ssid)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('.', end='')
        sleep(1)
    print('IP address:', wlan.ifconfig()[0])

def read_light():
    reading = sensor.read_u16()
    percent = int(reading / max_reading * 100)
    if percent > 100:
        percent = 100
    return percent

app = Microdot()
connect_wifi(ssid, password)

@app.route('/')
def index(request):
    return 'Light: ' + str(read_light())

app.run(port=80)
