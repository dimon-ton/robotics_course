# code control dc mortor

'''
devices as below
1. L298N (motor driver)
2. dc mortor
3. raspberry pi pico or esp32 or esp8266
4. battery 5-12 V
'''


from machine import Pin, PWM
from time import sleep

IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)
IN3 = Pin(4) # control speed pin

speed1 = PWM(IN3)
speed1.freq(150)

while True:
    #clockwise direction
    speed1.duty_u16(50000)
    IN1.high()
    IN2.low()
    sleep(3)
    
    # stop mortor
    IN1.low()
    IN2.low()
    sleep(2)
    
    
    
    #anit-clockwise direction
    speed1.duty_u16(25000)
    IN1.low()
    IN2.high()
    sleep(3)
    
    # stop mortor
    IN1.low()
    IN2.low()
    sleep(2)
