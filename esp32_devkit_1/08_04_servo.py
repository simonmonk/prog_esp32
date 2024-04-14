from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(18))
servo.freq(50) # pulse every 20ms

def set_angle(angle, min_pulse_us=500, max_pulse_us=2500):
    us_per_degree = (max_pulse_us - min_pulse_us) / 180
    pulse_us = us_per_degree * angle + min_pulse_us
    # duty 0 to 1023. At 50Hz, each duty_point is 20000/65535 = 0.305 µs/duty_point
    duty = int(pulse_us / 0.305)
    # print("angle=" + str(angle) + " pulse_us=" + str(pulse_us) + " duty=" + str(duty))
    print(angle)
    servo.duty_u16(duty)
    
def waggle():
    set_angle(10)
    sleep(0.5)
    set_angle(90)
    sleep(0.5)
    set_angle(170)
    sleep(0.5)
    set_angle(90)
    sleep(0.5)

while True:
    waggle()
    sleep(2)
    
