# https://gist.github.com/pdp7/1281d56fe9f1a2ff071fd02d2712420a
import Adafruit_BBIO.GPIO as GPIO
import time
 
value = 0
 
print 'linker button modle'
print 'linker button connected to digital port'
time.sleep(3)
 
GPIO.setup("P9_42",GPIO.IN)
 
while True:
    if GPIO.input("P9_42") == 0:
        value += 1
        print 'Press the button %2d times'%(value)
    time.sleep(0.2)



