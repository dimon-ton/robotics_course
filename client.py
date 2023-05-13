import network
import time
import socket
import utime
from machine import Pin
import random

# config LED
led_green = Pin(16, Pin.OUT)
led_yellow = Pin(18, Pin.OUT)
led_red = Pin(20, Pin.OUT)


led_green.off()
led_yellow.off()
led_red.off()


led_list = [(led_green, 'LED_GREEN'),
            (led_yellow, 'LED_YELLOW'),
            (led_red, 'LED_RED')]

# connect to network
wifi = "dimon's Galaxy S10e"
passwd = '12345678'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(1)

def send_data(data):
    serverip = '192.168.146.100'
    port = 9000
    
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server: ', data_server)
    server.close()
    
    
# send_data("hello World")
for i in range(10):
    select = random.choice(led_list)
    led = select[0]
    name = select[1]
    txt = '------{}--------'.format(name)
    led.on()
    send_data(txt)
    time.sleep(5)
    led.off()