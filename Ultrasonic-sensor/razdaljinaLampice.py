import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG=7 #definisem na kom GPIO-u su TRIG i ECHO
ECHO=36

GPIO.setup(TRIG,GPIO.OUT)  #definisem TRIG kao ulaz
GPIO.setup(ECHO,GPIO.IN)   #definisem ECHo kao ulaz
GPIO.setup(29,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

i=1

while i>0:
        GPIO.output(TRIG,0)  #TRIG-u dajem vrednost 0

        time.sleep(0.1)

        print "Merenje je pocelo!"

        GPIO.output(TRIG,1) #TRIG-u dajem vrednost 0
        time.sleep(0.00001)
        GPIO.output(TRIG,0) #TRIG-u dajem vrednost 1 kada pocinje rmitovanje signala sa predajnika

        while GPIO.input(ECHO)==0:
            pass
        start= time.time() #ocitava vreme 

        while GPIO.input(ECHO)==1:
            pass
        stop=time.time() #ocitava vreme 

        print ""
        print "Razdaljina je:"

        print (stop-start)*17000 ,"cm"

        if ((stop-start)*17000)<10:
            GPIO.output(29,True)
            GPIO.output(11,False)
            GPIO.output(15,False)
            GPIO.output(16,False)
        elif ((stop-start)*17000)<20:            
            GPIO.output(11,True)
            GPIO.output(29,False)
            GPIO.output(15,False)
            GPIO.output(16,False)
        elif((stop-start)*17000)<30:
            GPIO.output(15,True)
            GPIO.output(29,False)
            GPIO.output(11,False)
            GPIO.output(16,False)
        else:
            GPIO.output(16,True)
            GPIO.output(29,False)
            GPIO.output(11,False)
            GPIO.output(15,False)

GPIO.cleanup()

