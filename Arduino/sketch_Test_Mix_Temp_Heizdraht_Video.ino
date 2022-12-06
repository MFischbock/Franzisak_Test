// Temperatur soll ständig gemessen werden und über die Zeit ansteigen (Potentiometer, Relais oder Transistor?) -> Stirnband erhitzt sich
// Relay und Transistor -> Intervallschaltung, um zu heizen.
// bei einer bestimmten Temp. stoppt das Videobild mit dem laufenden Körper
// nach einem bestimmten Zeitraum stagniert auch die Temperatur und ein Wassertropfen soll über die Stirn laufen -> Magnetventil (aber wie kommt das Wasser ans Strinband?)

#include <OneWire.h>
#include <DallasTemperature.h>

int strom = A0; //Das Wort „Strom“ steht jetzt für den Wert „A0“ (Bezeichnung vom Analogport 0)Potentiometer/Transistor/Relay, connected zum Heizdraht.
int heizdraht; // Dieser muss erhitzt werden über Strom
int TMP36 = 2; //Der Sensor soll am analogen Pin 2 angeschlossen werden. Wir nennen den Pin ab jetzt "TMP36" Temperatursensor
int sensorwert; 
int temperatur = 0; //Unter der Variablen "temperatur" wird später der Temperaturwert abgespeichert.
int t=500; //Der Wert für „t“ gibt im Code die zeitlichen Abstände zwischen den einzelnen Messungen vor.
int videobild=5; //Das Wort „videobild“ steht jetzt für die Zahl 5, also wird an Pin5 die Videoübertragung gestoppt. 

void setup() 
{
Serial.begin(9600);
pinMode (videobild, OUTPUT); //Der Pin für das Video wird als Ausgang definiert, da hier, um das Video zu stoppen, eine Spannung benötigt wird.
pinMode (strom, INPUT); //Der Pin mit der Stromstärke Volt und mA Steuerung (PIN A0) um Heizdraht zu erhitzen ist jetzt ein Eingang.
pinMode (heizdraht, OUTPUT); 
}

void loop() 
{
sensorwert =analogRead(strom); //Die Spannung am Drehregler wird ausgelesen und wie im vorherigen Sketch als Zahl zwischen 0 und 1023 unter der Variable „sensorwert“ gespeichert.
digitalWrite (heizdraht, HIGH); //Der Heizdraht wird erhitzt.
delay (sensorwert); //Der Heidraht bleibt für so viele Millisekunden aufgeheizt, wie der Wert von „sensorwert“ es gespeichert hat
digitalWrite (heizdraht, LOW); //Der Heizdraht kühlt ab.
delay (sensorwert); //Der Heizdraht bleibt für so viele Millisekunden kalt, wie der Wert von „sensorwert“ es gespeichert hat.
}
//Der Loop-Teil wird nun erneut gestartet. Wenn sich der Wert des ausgelesenen Drehreglers ändert, dann ändert sich auch die Zeit zwischen den Ein- und Aus-Phasen der LED. Das Blinken wird dadurch schneller und langsamer. Das längste delay beträgt in diesem Sketch 1023ms (Millisekunden). Wenn man längere delays benötigt, dann baut man eine kleine mathematische Zeile in den Code ein. Beispiel: Man ändert die Zeile „sensorwert =analogRead(eingang);“ in „sensorwert =analogRead(eingang)*2;“ Damit wird der abgespeicherte Sensorwert um den Faktor 2 vergrößert. Da längste delay wäre dann 2046ms usw…

sensorwert=analogRead(TMP36); 
temperatur= map(sensorwert, 0, 410, -50, 150);
delay(t);
Serial.print(temperatur);
Serial.println(" Grad Celsius");

if (temperatur>=30) //Es wird eine IF-Bedingung erstellt: Wenn der Wert für die Temperatur über oder gleich 30 ist, dann…
{
digitalWrite(videobild,HIGH); //…stoppe das laufende Männchen.
}

else //Und wenn das nicht so ist…
{
digitalWrite(videobild,LOW); //…dann läuft das Männchen.
}
}
