from machine import Pin, I2C, RTC
from ssd1306 import SSD1306_I2C
from math import sin, cos, radians
from time import sleep
from network import WLAN, STA_IF
import ntptime
import datetime

ssid = 'network'      # CHANGE ME
password = 'password' # CHANGE ME

tz = datetime.timezone(datetime.timedelta(hours=0))

i2c = I2C(0, sda=Pin(19, pull=Pin.PULL_UP),
          scl=Pin(18, pull=Pin.PULL_UP))
oled = SSD1306_I2C(128, 64, i2c)

origin_x = 32
origin_y = 31

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def message(text, delay=0):
    oled.fill(0)
    oled.text(text, 0, 20)
    oled.show()
    sleep(delay)

def connect_wifi(ssid, password):
    wlan = WLAN(STA_IF)
    wlan.active(True)
    message('connect ' + ssid)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('.', end='')
        sleep(1)
    print('IP address:', wlan.ifconfig()[0])
    

def show_time(dt):
    oled.fill(0)
    draw_face()
    draw_hand((dt.hour + dt.minute / 60) * 5, 16)
    draw_hand(dt.minute + dt.second / 60, 20)
    draw_hand(dt.second, 25)
    draw_date(dt, 70, 10)
    oled.show()
    
def draw_date(dt, x, y):
    date_str = str(dt.day) + ' ' + months[dt.month-1]
    year_str = str(dt.year)
    oled.text(date_str, x, y, 1)
    oled.text(year_str, x, y+40, 1)
    
def polar_rect(angle, radius):
    x = int(radius * sin(radians(angle)))
    y = -int(radius * cos(radians(angle)))
    return x, y
    
def draw_hand(minutes, radius):
    angle = (360 / 60) * minutes 
    x, y = polar_rect(angle, radius)
    oled.line(origin_x, origin_y, origin_x+x, origin_y+y, 1)

def draw_face():
    for hour in range(0, 12):
        x, y = polar_rect(hour * 30, 28)
        hour_str = str(hour)
        if hour == 0:
            hour_str = '12'
        if hour > 9 or hour == 0:
            x -= 3
        oled.text(hour_str, origin_x+x-4, origin_y+y-3, 1)

def set_time():
    connect_wifi(ssid, password)
    message('UPDATING ....')
    try:
        ntptime.settime()
        message('Update Success', delay=2)
    except:
        message('NTP fail', delay=2)
    oled.show()

set_time()

while True:
    t = datetime.datetime.now(tz)
    if t.hour == 1 and t.minute == 0 and t.second == 0:
        set_time()
    show_time(t)
    sleep(0.1)
    