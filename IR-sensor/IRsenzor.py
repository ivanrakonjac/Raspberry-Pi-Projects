import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

SENZOR=7 #definisem na kom GPIO-u 
DIODA=16

GPIO.setup(16,GPIO.OUT)  
GPIO.setup(7,GPIO.IN)  

if GPIO.input(7)==1:
        pass
        GPIO.output(16,True)
else:   
        pass
        GPIO.output(16,False)

GPIO.cleanup()

