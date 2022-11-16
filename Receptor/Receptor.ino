#include <Wire.h>
#include <SPI.h>
#include <nRF24L01.h>     
#include <RF24.h>

unsigned long timeReal = 0;
float dataPacket[7];
String comma = ",";

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
    radio.read(&dataPacket, sizeof(dataPacket));

    // PACKET1
    if (dataPacket[0] == 0){
      alt = dataPacket[1];
      pres = dataPacket[2];
      temp = dataPacket[3];
    }
    else {
      // PACKET2
      ax = dataPacket [1];
      ay = dataPacket [2];
      az = dataPacket [3];
      gx = dataPacket [4];
      gy = dataPacket [5];
      gz = dataPacket [6];
    }

    // Sending data through Serial (0.5 s)
    if (micros() - timeReal >= 500000){
      Serial.println(alt + comma + pres + comma + temp + comma + ax + comma + ay + comma + az + comma + gx + comma + gy + comma + gz);
      timeReal = micros(); 
    }
  }
}