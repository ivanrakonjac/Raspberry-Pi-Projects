#include <stdio.h>
#include <wiringPi.h>

#define LED 22


int main()  
{
	int i=0;
	printf("Stampaj!\n");
	wiringPiSetupGpio();
	pinMode(LED,OUTPUT);
	
	while(i<5){
		digitalWrite(LED,HIGH);
		delay(500);
		digitalWrite(LED,LOW);
		delay(500);
		i++;
		}
		digitalWrite(LED,LOW);
		printf("Gasim!\n");
	return 0;
}

