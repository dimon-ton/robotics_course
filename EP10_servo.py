from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(28))
pwm.freq(50)


# for i in range(0, 3000, 5): 
#     pwm.duty_u16(i)
#     print(i)
#     sleep(1)

# for position in range(1400, 8400, 100):
#     pwm.duty_u16(position)
#     print(position)
#     sleep(2)


pwm.duty_u16(4790)