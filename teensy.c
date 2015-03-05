#include "DHT.h"
#define DHTPIN 8     	// what pin we're connected to
#define DHTTYPE DHT11   // DHT 11 

DHT dht(DHTPIN, DHTTYPE);

void setup () {
	Serial.begin(9600);
	dht.begin;
	} 

void loop() {

  if (Serial.available())    {

     int ch = Serial.read();

     if ( ch == '1' ) {
		float h = dht.readHumidity();
		float t = dht.readTemperature();
		
		if (isnan(h) || isnan(t)) {
			Serial.println("Failed to read from DHT sensor!");
			return;
		}
		Serial.print(h);
		Serial.print(",");
		Serial.println(t);
     } else {
       delay(10);
     }
   }    
}
