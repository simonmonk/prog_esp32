from network import WLAN, STA_IF
from microdot import Microdot
from time import sleep

ssid = 'network'      # CHANGE ME
password = 'password' # CHANGE ME

def connect_wifi(ssid, password):
    wlan = WLAN(STA_IF)
    wlan.active(True)
    print('connecting to ' + ssid)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('.', end='')
        sleep(1)
    print('IP address:', wlan.ifconfig()[0])

app = Microdot()  
connect_wifi(ssid, password)

@app.route('/') # Handler for the root page
def index(request):
    return 'Hello from ESP32'

app.run(port=80)