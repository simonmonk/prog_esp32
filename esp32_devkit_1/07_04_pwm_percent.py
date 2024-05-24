from machine import Pin, PWM
from time import sleep

led = PWM(Pin(22))

while True:
    brightness_str = input('brightness (0-100):')
    brightness = int(int(brightness_str) * 65535 / 100)
    led.duty_u16(brightness)