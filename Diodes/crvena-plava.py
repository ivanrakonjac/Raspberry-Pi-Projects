import RPi.GPIO as GPIO
import os
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

ledChoice=0
count=0

os.system('clear')
print "Koju diodu zelis da upalis?"
print"1: Crevenu?"
print"2: Plavu?"

ledChoice=input("Odaberi koju diodu zelis:")

if ledChoice == 1:
    os.system ('clear')
    print "Upalice se CRVENA."
    count=input("Koliko puta da se upali?: ")
    while count>0 :
            GPIO.output(7,True)
            time.sleep(1)
            GPIO.output(7,False)
            time.sleep(1)
            count=count-1



if ledChoice == 2:
    os.system ('clear')
    print "Upalice se PLAVA."
    count=input("Koliko puta da se upali?: ")
    while count>0 :
            GPIO.output(16,True)
            time.sleep(1)
            GPIO.output(16,False)
            time.sleep(1)
            count=count-1



if ledChoice !=1 or 2 :
        print "UNESI 1 ili 2!"
    
    
