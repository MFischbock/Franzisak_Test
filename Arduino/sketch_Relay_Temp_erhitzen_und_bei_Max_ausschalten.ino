//Temperatur erhitzen und bei Max Temp. ausschalten mit Relay -> (öffnen und schließen des Stromkreislaufes -> also das Intervall steuern?)

#include <OneWire.h>
#include <DallasTemperature.h>

#define SENSOR_PIN  2   // Arduino pin connected to DS18B20 sensor's DQ pin
#define RELAY_PIN   A5  // Arduino pin connected to relay which connected to heating element

const int TEMP_THRESHOLD_UPPER = 26; // upper threshold of temperature, change to your desire value -> hier brauchen wir die genauen Daten des Heißdrahtes, max. temp.
const int TEMP_THRESHOLD_LOWER = 15; // lower threshold of temperature, change to your desire value -> hier die Ausgangstemperatur 

OneWire oneWire(SENSOR_PIN);         // setup a oneWire instance
DallasTemperature sensors(&oneWire); // pass oneWire to DallasTemperature library

float temperature;    // temperature in Celsius

void setup() {
  Serial.begin(9600); // initialize serial
  sensors.begin();    // initialize the sensor
  pinMode(RELAY_PIN, OUTPUT); // initialize digital pin as an output
}

void loop() {
  sensors.requestTemperatures();             // send the command to get temperatures
  temperature = sensors.getTempCByIndex(0);  // read temperature in Celsius

  if(temperature > TEMP_THRESHOLD_UPPER) {
    Serial.println("The heating element is turned off");
    digitalWrite(RELAY_PIN, LOW); // turn off
  } else if(temperature < TEMP_THRESHOLD_LOWER){
    Serial.println("The heating element is turned on");
    digitalWrite(RELAY_PIN, HIGH); // turn on
  }

  delay(500);
}
