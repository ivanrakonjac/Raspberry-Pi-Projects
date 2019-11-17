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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

pauza=0.002;
x=0;

i=1;

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

            for x in range (0,128): # 512 = 360 stepeni
                    GPIO.output(29,False)
                    GPIO.output(31,False)
                    GPIO.output(33,False)
                    GPIO.output(35,True)
                    time.sleep(pauza)
                    GPIO.output(29,False)
                    GPIO.output(31,False)
                    GPIO.output(33,True)
                    GPIO.output(35,False)
                    time.sleep(pauza)
                    GPIO.output(29,False)
                    GPIO.output(31,True)
                    GPIO.output(33,False)
                    GPIO.output(35,False)
                    time.sleep(pauza)
                    GPIO.output(29,True)
                    GPIO.output(31,False)
                    GPIO.output(33,False)
                    GPIO.output(35,False)
                    print "IDEM NAZAD"
                    time.sleep(pauza)
                    
        elif ((stop-start)*17000)<20:            
            GPIO.output(11,True)
            GPIO.output(29,False)
            GPIO.output(15,False)
            GPIO.output(16,False)

            for x in range (0,128): # 512 = 360 stepeni
                    GPIO.output(29,False)
                    GPIO.output(31,False)
                    GPIO.output(33,False)
                    GPIO.output(35,True)
                    time.sleep(pauza)
                    GPIO.output(29,False)
                    GPIO.output(31,False)
                    GPIO.output(33,True)
                    GPIO.output(35,False)
                    time.sleep(pauza)
                    GPIO.output(29,False)
                    GPIO.output(31,True)
                    GPIO.output(33,False)
                    GPIO.output(35,False)
                    time.sleep(pauza)
                    GPIO.output(29,True)
                    GPIO.output(31,False)
                    GPIO.output(33,False)
                    GPIO.output(35,False)
                    print "IDEM NAZAD"
                    time.sleep(pauza)
                    
        elif((stop-start)*17000)<30:
            GPIO.output(15,True)
            GPIO.output(29,False)
            GPIO.output(11,False)
            GPIO.output(16,False)

            for x in range (0,128): # 512 = 360 stepeni
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
                    print "kRECEM SE NAPRED!"
                    time.sleep(pauza)
        else:
            GPIO.output(16,True)
            GPIO.output(29,False)
            GPIO.output(11,False)
            GPIO.output(15,False)
            
            for x in range (0,128): # 512 = 360 stepeni
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
                    print "kRECEM SE NAPRED!"
                    time.sleep(pauza)
                    

