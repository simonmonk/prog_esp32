from machine import Pin, PWM

led = PWM(Pin(22))

while True:
    brightness_str = input("brightness (0-65535):")
    brightness = int(brightness_str)
    led.duty_u16(brightness)
    