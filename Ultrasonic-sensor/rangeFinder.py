import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG=7 #definisem na kom GPIO-u su TRIG i ECHO
ECHO=36

GPIO.setup(TRIG,GPIO.OUT)  #definisem TRIG kao ulaz
GPIO.setup(ECHO,GPIO.IN)   #definisem ECHo kao ulaz


while True:
    choice = raw_input("> ")

    if choice != 'b' : #ako pritisnmes b program staje
        


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

        time.sleep(1)
    
    

GPIO.cleanup()

