from network import WLAN, STA_IF
import urequests
import json
from time import sleep

ssid = 'network'
password = 'password'
key = 'ea751fc7712f27059e8agh99445453b712'
location = 'lat=53.925854&lon=-3.021994'
api_base = 'http://api.openweathermap.org/data/2.5/weather?'
url = api_base + location + '&appid=' + key

def connect_wifi(ssid, password):
    wlan = WLAN(STA_IF)
    wlan.active(True)
    print('connecting to ' + ssid)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('.', end='')
        sleep(1)
    print('IP address:', wlan.ifconfig()[0])

def get_weather():
    global response
    response = urequests.get(url)
    if (response.status_code == 200):
        data = json.loads(response.text)
        description = data['weather'][0]['description']
#     print(data)
        temp = int(data['main']['temp'] - 273.15)
        print('temperature {}C: ({})'.format(temp, description))
    else:
        print('Web service unavailable: ' + str(response.reason, 'utf-8'))

connect_wifi(ssid, password)
get_weather()

