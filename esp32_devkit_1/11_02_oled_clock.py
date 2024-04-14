from machine import Pin, I2C, RTC
from ssd1306 import SSD1306_I2C
from math import sin, cos, radians
from time import sleep, localtime

i2c = I2C(0, sda=Pin(19, pull=Pin.PULL_UP),
          scl=Pin(21, pull=Pin.PULL_UP))
oled = SSD1306_I2C(128, 64, i2c)

origin_x = 32
origin_y = 31

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def show_time():
    oled.fill(0)
    draw_face()
    dt = localtime()
    hour, minute, second = dt[4], dt[5], dt[6]
    draw_hand((hour + minute / 60) * 5, 16)
    draw_hand(minute + second / 60, 20)
    draw_hand(second, 25)
    draw_date(dt, 70, 10)
    oled.show()
    
def draw_date(dt, x, y):
    day, month, year = dt[2], dt[1], dt[0]
    date_str = str(day) + ' ' + months[month-1]
    year_str = str(year)
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

while True:
    show_time()
    sleep(0.1)
