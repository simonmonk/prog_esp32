from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(21, pull=Pin.PULL_UP),
          scl=Pin(22, pull=Pin.PULL_UP))

oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.rect(0, 0, 127, 63, 1)
oled.text('Programming the', 5, 12, 1)
oled.text('ESP32', 5, 22, 1)
oled.text('by', 5, 32, 1)
oled.text('Simon Monk', 5, 42, 1)

oled.show()