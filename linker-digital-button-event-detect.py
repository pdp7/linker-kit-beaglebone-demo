# https://gist.github.com/pdp7/30bab7029b9faab34a33b80620bc4d59
import Adafruit_BBIO.GPIO as GPIO
import time
 
def process_event(channel):  
    print("Processing event for channel {0}".format(channel))

print('linker button connected to digital port')
GPIO.setup("P9_42", GPIO.IN)
GPIO.add_event_detect("P9_42", GPIO.FALLING, callback=process_event)
print('waiting for button press event')
time.sleep(300)

