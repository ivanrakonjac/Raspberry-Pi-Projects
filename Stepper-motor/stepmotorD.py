import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

pauza=0.002

for x in range (0,256): # 512 = 360 stepeni
    GPIO.output(29,True)
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(35,False)
    time.sleep(pauza)
    GPIO.output(29,False)
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(35,False)
    time.sleep(pauza)
    GPIO.output(29,False)
    GPIO.output(31,False)
    GPIO.output(33,True)
    GPIO.output(35,False)
    time.sleep(pauza)
    GPIO.output(29,False)
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(35,True)
    time.sleep(pauza)
GPIO.cleanup()
    
