# servo specicfication
# MG90s

from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(28))
pwm.freq(50)

# default value
# max_range = 8400
# min_range = 1400

max_range = 8400
min_range = 1400

while True:
    for position in range(min_range, max_range, 100):
        pwm.duty_u16(position)

        sleep(0.01)
        
    for position in range(max_range, min_range, -100):
        pwm.duty_u16(position)

        sleep(0.01)