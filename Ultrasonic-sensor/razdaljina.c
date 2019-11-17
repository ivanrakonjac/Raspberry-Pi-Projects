#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define LED_P 23
#define LED_C 17
#define LED_ZU 18
#define LED_ZE 22

#define TRIG 4
#define ECHO 16

void ponisti(){
	digitalWrite(LED_C,LOW);
	digitalWrite(LED_ZE,LOW);
	digitalWrite(LED_ZU,LOW);
	digitalWrite(LED_P,LOW);
}

void provera(int distance){
	if(distance>30){
		digitalWrite(LED_P,HIGH);
		digitalWrite(LED_C,LOW);
		digitalWrite(LED_ZU,LOW);
		digitalWrite(LED_ZE,LOW);
	}
	else if((distance<30)&&(distance>20)){
		digitalWrite(LED_ZE,HIGH);
		digitalWrite(LED_C,LOW);
		digitalWrite(LED_ZU,LOW);
		digitalWrite(LED_P,LOW);
	}
	else if((distance<20)&&(distance>10)){
		digitalWrite(LED_ZU,HIGH);
		digitalWrite(LED_C,LOW);
		digitalWrite(LED_ZE,LOW);
		digitalWrite(LED_P,LOW);
	}
	else if(distance<10){
		digitalWrite(LED_C,HIGH);
		digitalWrite(LED_ZE,LOW);
		digitalWrite(LED_ZU,LOW);
		digitalWrite(LED_P,LOW);
	}
}

int main(int argc, char **argv)
{
	int i=0;
	float min=100,max=0;
	
	wiringPiSetupGpio();
	pinMode(LED_P,OUTPUT);
	pinMode(LED_C,OUTPUT);
	pinMode(LED_ZU,OUTPUT);
	pinMode(LED_ZE,OUTPUT);
	
	pinMode(TRIG,OUTPUT);
	pinMode(ECHO,INPUT);
	
	ponisti();
	
	while(i<100){
		//dajem trigu vrednost 0
		digitalWrite(TRIG,LOW);
		delay(30);
		printf("**************************\n");
		printf("\nMerenje pocinje!\n");
		//merenje
		digitalWrite(TRIG,HIGH);
		delayMicroseconds(500);
		digitalWrite(TRIG,LOW);
		
		while (digitalRead(ECHO)==LOW);
		float startTime=micros();
		while (digitalRead(ECHO)==HIGH);
		float travelTime=micros()-startTime;
		
		float distance=travelTime*0.017;
		printf("\nDistanca je: %fcm\n",distance);
		
		provera(distance);
		
		if(distance<min){
			min=distance;
		}
		if(distance>max){
			max=distance;
		}
		
		i++;
	}
	printf("**************************\n");
	ponisti();
	printf("\nNajdalja pozicija je je: %fcm\n",max);
	printf("\nNajbliza pozicija je: %fcm\n",min);
	
	return 0;
}

