from machine import Pin
from time import sleep

led = Pin('LED', Pin.OUT)


for i in range(20):
    led.on()
    sleep(2)
    led.off()
    sleep(1)
    
    

