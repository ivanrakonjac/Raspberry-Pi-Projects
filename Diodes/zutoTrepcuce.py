import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
x=0
while x<10 :
    GPIO.output(11,True)
    time.sleep(0.5)
    GPIO.output(11,False)
    time.sleep(0.5)
    x=x+1;    
GPIO.cleanup()
