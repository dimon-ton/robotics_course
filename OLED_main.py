# convert img to base64code --> https://gurgleapps.com/tools/image-to-code?fbclid=IwAR0eJ-G563WiC9tsfbEeM5i1bPAJUq_jiFCX4XeyBG20L6DRs1teDzvEvbw
# github.com --> https://github.com/gurgleapps/image-to-code/
# dimension --> 128x64

from machine import Pin, I2C
import ssd1306
import time
import framebuf
import base64

i2c = I2C(0, sda=Pin(16), scl=Pin(17))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

robot = 'gED////////////////////////////+AAAAAP/////////////wAAAAAAAAH//////////4AAAAAAAAAAAf///////+AAAAAAAAAAAAAH//////wAAAAAAAAAAAAAAD////8AAAAAAAAAAAAAAAAA///4AAAAAAAAAAAAAAAAAB//4AAAAAAAAAAAAAAAAAAH/8AAAAAAAAAAAAAAAAAAA/+AAAAAAAAAAAAAAAAAAAH/AAAAAAAAAAAAAAAAAAAA/wAAAAAAAAAAAAAAAAAAAP4AAAAAAAAAAAAAAAAAAAB8AAAAAAAAAAAAAAAAAAAAPAAAAD/gAAAAAAAD/gAAADwAAAD/+AAAAAAAD/+AAAA8AAAB//wAAAAAAB//wAAAOAAAB///AAAAAAB///AAABgAAAf//wAAAAAAf//wAAAYAAAP//+AAAAAAP//+AAAGAAAH///wAAAAAH///wAABgAAB///8AAAAAB///8AAAYAAAf///AAAAAAf///AAAGAAAP///4AAAAAP///4AABgAAD///+AAAAAD///+AAAYAAA////gAAAAA////gAAGAAAP///4AAAAAP///4AABgAAD///+AAAAAD///+AAAYAAA////gAAAAA////gAAGAAAH///wAAAAAH///wAABgAAB///8AAAAAB///8AAAYAAAf///AAAAAAf///AAAGAAAD///gAAAAAD///gAABgAAAf//wAAAAAAf//wAAAYAAAH//8AAAAAAH//8AAAGAAAAf/8AAAAAAAf/8AAABgAAAD/+AAAAAAAD/+AAAAYAAAAP+AAAAAAAAP+AAAAGAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAGAAAAAAADAAAAGAAAAAAABgAAAAAAB4AAADwAAAAAAAYAAAAAAAfAAAB8AAAAAAAGAAAAAAAD4AAA+AAAAAAABgAAAAAAA/AAAfAAAAAAAAcAAAAAAAH4AAfwAAAAAAAPAAAAAAAA/AAP4AAAAAAADwAAAAAAAH+Af8AAAAAAAA8AAAAAAAA///8AAAAAAAAPgAAAAAAAD//+AAAAAAAAH8AAAAAAAAP/8AAAAAAAAD/AAAAAAAAA/8AAAAAAAAA/4AAAAAAAAAAAAAAAAAAAf/AAAAAAAAAAAAAAAAAAAP/4AAAAAAAAAAAAAAAAAAH//gAAAAAAAAAAAAAAAAAH///AAAAAAAAAAAAAAAAAP////////////////////////////////////////////'
blink = 'gEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB/////wAAAAAAAAAAAAAH////////4AAAAAAAAAAH///////////gAAAAAAAB/////////////4AAAAAAP//////////////8AAAAD/////////////////AAAH/////////////////+AAH//////////////////4AD///////////////////AB///////////////////4A////////////////////AP///////////////////wH///////////////////+D////////////////////w////////////////////8P////////////////////D//P///////////////P/x//h///////////////h/+f/4H//////////////gf/n//A//////////////wP/5//4D/////////////wH/+f//AP////////////wD//n//4A////////////wB//5///gA///////////AB//+f//8AAAH//////AAAB///n///4AAAf/////gAAB///5////gAAH/////4AAB///+f///gAAB/////+AAAH///n///gAAB//////4AAAf//5///wA///////////AD//+f//wD////////////Af//n//4D////////////8B//5//8D/////////////wP/+f//B/////////////+D//n//g//////////////wf/5//wf/////////////+D/+f/8P//////////////w//n//n//////////////+f/5////////////////////+f////////////////////n////////////////////5////////////////////+f////////////////////n////////////////////5////////////////////+f////////////////////n////////n//5////////5////////w//8P///////+f///////8H/+D////////j////////h//h////////w////////4P/wf///////8P////////D/4P////////D////////wf8D////////wf///////+B8B////////4D////////wAA////////8A////////+AAf////////AH////////wAf////////gA/////////Af////////wAH//////////////////4AAf/////////////////4AAA/////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

def custom_to_buff(data):
    width = data[0]
    height = data[1]
    
    fbuff = framebuf.FrameBuffer(data[2:], width, height, framebuf.MONO_HLSB)
    return fbuff

def show_image(image):
    display.blit(image, 0, 0)
    display.show()
    
robot_image = custom_to_buff(bytearray(base64.b64decode(robot)))
blink_image = custom_to_buff(bytearray(base64.b64decode(blink)))

while True:
     display.fill(0)
     show_image(robot_image)
     time.sleep(2)
     show_image(blink_image)
     time.sleep(2)
     
     
     
     

