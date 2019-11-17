#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define PIN 6

int main()
{
	//int i=0;
	
	while (1){
	   
	   wiringPiSetupGpio();
	   pinMode (PIN, OUTPUT) ;
	   pwmSetMode (PWM_MODE_MS);
	   pwmSetRange (2000);
	   pwmSetClock (192);
	   pwmWrite(PIN,150);
	   delay(1000);
	   pwmWrite(PIN,200);
	   
   }
   return 0;

}


