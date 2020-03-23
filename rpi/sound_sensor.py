import time
import RPi.GPIO as GPIO

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

while 1:
    pin_val = GPIO.input(pin)
    print("pin val = ", pin_val)
    if GPIO.input(pin) == GPIO.LOW:
       # print("sound low")
       h = 7
    else:
        print("Sound High")
        
    time.sleep(0.5)
