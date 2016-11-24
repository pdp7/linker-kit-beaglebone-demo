# https://gist.github.com/pdp7/c3933591d6f662a299aedba57c1178b0
import Adafruit_BBIO.GPIO as GPIO
import time
 
print('linker button connected to digital port')
 
GPIO.setup("P9_42", GPIO.IN)

print('Press and hold button')
channel = GPIO.wait_for_edge("P9_42", GPIO.FALLING)
print('<edge detected on channel>')

print('Release button')
channel = GPIO.wait_for_edge("P9_42", GPIO.RISING)
print('<edge detected on channel>')

