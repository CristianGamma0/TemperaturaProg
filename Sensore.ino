#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

int soglia = 26;
int pinR = 3;
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  // put your setup code here, to run once:
  pinMode(pinR, OUTPUT);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  auto t = dht.readTemperature();
  auto u = dht.readHumidity();
  Serial.print(t);
  Serial.print(";");
  Serial.println(u);
  if(t >= soglia){
    digitalWrite(pinR, HIGH);
  }else{
    digitalWrite(pinR, LOW);
  }
  delay(1000);
}
