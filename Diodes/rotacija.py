import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
x=0
while 1 :
    GPIO.output(7,True)
    time.sleep(0.2)
    GPIO.output(7,False)
    time.sleep(0.2)
    GPIO.output(16,True)
    time.sleep(0.2)
    GPIO.output(16,False)
    time.sleep(0.2)
    
    
