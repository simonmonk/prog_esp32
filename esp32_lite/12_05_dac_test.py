from machine import DAC, Pin

dac = DAC(Pin(25))

while True:
    volt_str = input('Enter Voltage (0 to 3.3):')
    try:
        volt = float(volt_str)
        value = int(volt / 3.3 * 255.0)
        dac.write(value)
    except:
        print('bad voltage value')