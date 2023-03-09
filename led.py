from machine import Pin
from utime import sleep_ms

red = Pin(20, Pin.OUT)
yellow = Pin(18, Pin.OUT)
green = Pin(16, Pin.OUT)

all_led = [red, yellow, green]

while True:
    for led in all_led:
        led.on()
        sleep_ms(500)
        led.off()
        sleep_ms(500)