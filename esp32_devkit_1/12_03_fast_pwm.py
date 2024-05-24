from machine import Pin, PWM

out_pin = PWM(Pin(32))
out_pin.freq(1000000) # 1MHz

out_pin.duty_u16(32000) # 50%
