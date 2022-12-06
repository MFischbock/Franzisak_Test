//Temperatur erhitzen und bei Max Temp. ausschalten mit Relay -> (öffnen und schließen des Stromkreislaufes -> also das Intervall steuern?)

#include <OneWire.h>
#include <DallasTemperature.h>

#define SENSOR_PIN  2   // Arduino pin connected to DS18B20 sensor's DQ pin
#define fadePin 9  // Arduino pin connected to relay which connected to heating element

const int TEMP_THRESHOLD_UPPER = 32; // upper threshold of temperature, change to your desire value -> hier brauchen wir die genauen Daten des Heißdrahtes, max. temp.
const int TEMP_THRESHOLD_LOWER = 20; // lower threshold of temperature, change to your desire value -> hier die Ausgangstemperatur 

OneWire oneWire(SENSOR_PIN);         // setup a oneWire instance
DallasTemperature sensors(&oneWire); // pass oneWire to DallasTemperature library

float temperature;    // temperature in Celsius

void setup() {
  Serial.begin(9600); // initialize serial
  sensors.begin();    // initialize the sensor
  pinMode(fadePin, OUTPUT); // initialize digital pin as an output
}

void loop() {
  for(int i = 0; i<360; i++){
    //convert 0-360 angle to radian (needed for sin function)
    float rad = DEG_TO_RAD * i;

    //calculate sin of angle as number between 0 and 255
    int sinOut = constrain((sin(rad) * 128) + 128, 0, 255); 

    analogWrite(fadePin, sinOut);

  }
  Serial.println("funktioniert3");
  sensors.requestTemperatures();             // send the command to get temperatures
  temperature = sensors.getTempCByIndex(0);  // read temperature in Celsius

  if(temperature > TEMP_THRESHOLD_UPPER) {
    Serial.println("The heating element is turned off");
    digitalWrite(fadePin, LOW); // turn off
  } else if(temperature < TEMP_THRESHOLD_LOWER){
    Serial.println("The heating element is turned on");
    digitalWrite(fadePin, HIGH); // turn on
  }

  delay(500);
}
