from machine import Pin, Signal
led = Signal(22, Pin.OUT, invert=True)
led.on()
