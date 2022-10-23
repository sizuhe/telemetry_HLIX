#include <Wire.h>
#include <SPI.h>
#include <nRF24L01.h>     
#include <RF24.h>

unsigned long tiempoactual = 0;
float datos[7];    // Array con 8 variables
String coma = ",";   // Pues, es una coma

// Create an RF24 object
RF24 radio(9, 8);  // CE, CSN

// Address through which two modules communicate.
const byte address[6] = "00001";

// =============

void setup()
{
  Serial.begin(9600);
  radio.begin();
  
  // Set the address
  radio.openReadingPipe(0, address);
  
  // Set module as receiver
  radio.startListening();
}

// =============

void loop()
{     
  float alt,pres,temp,gx,gy,gz,ax,ay,az;
  
  // Read the data if available in buffer
  if (radio.available())
  {
    radio.read(&datos, sizeof(datos));

    // PACKET1
    if (datos[0] == 0){
      alt = datos[1];
      pres = datos[2];
      temp = datos[3];
    }
    else {
      // PACKET2
      ax = datos [1];
      ay = datos [2];
      az = datos [3];
      gx = datos [4];
      gy = datos [5];
      gz = datos [6];
    }

    // Impresion de los datos
    // Un segundo en microsegundos = 1000000
    if (micros() - tiempoactual >= 500000){
      Serial.println(alt + coma + pres + coma + temp + coma + ax + coma + ay + coma + az + coma + gx + coma + gy + coma + gz + coma);
      tiempoactual = micros(); 
    }
  }
}