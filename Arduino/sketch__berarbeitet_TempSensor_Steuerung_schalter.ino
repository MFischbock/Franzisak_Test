#include <OneWire.h>
#include <DallasTemperature.h>
#include <dht.h>
dht DHT;
//=============================================================================
#define DHT11_PIN 7 //==> SensorDaten-Pin für TemperaturSensor DHT11

#define Relais_PIN 6 //==> Pin für Relais 

#define Knopf_PIN 2 //==> Pin für den Knopf

#define start 18 //==> Start/Soll Temperatur

#define min 15 //==> Temperatur minimum

#define max 30 //==> Temperatur maximum
//=============================================================================
int knopf;
int soll_Temp;

OneWire oneWire(DHT11_PIN);
DallasTemperature sensors(&oneWire);

float temperature; //Temperatur in Celsius

void setup(){
  Serial.begin(9600);
  sensors.begin();
  pinMode(Relais_PIN, OUTPUT);
  digitalWrite(Relais_PIN,HIGH);
  pinMode(Knopf_PIN,INPUT_PULLUP);
}

void loop(){
  sensors.requestTemperatures();             // send the command to get temperatures
  temperature = sensors.getTempCByIndex(0);  // read temperature in Celsius
  if (soll_Temp == 0){
      soll_Temp = start;
  } 
  knopf = digitalRead(Knopf_PIN); 
  if (knopf == 0){
  soll_Temp = soll_Temp + 1;
  }
  if (soll_Temp > max){
      soll_Temp = min;
  }
  int chk = DHT.read11(DHT11_PIN);
  lcd.setCursor(0,0);
  lcd.print("Aktuell: ");
  lcd.print((float)DHT.temperature,0);
  lcd.print("\337C ");
  lcd.setCursor(0,1);
  lcd.print("Soll: ");
  lcd.print(soll_Temp);
  lcd.print("\337C ");
   if(DHT.temperature >= soll_Temp){
    lcd.setCursor(0,3);
    lcd.print("Status:Ausgeschaltet");
    digitalWrite(Relais_PIN,HIGH);
   }else{
    lcd.setCursor(0,3);
    lcd.print("Status:Eingeschaltet");
    digitalWrite(Relais_PIN,LOW);
   }
  delay(500);
}
