#include <Wire.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Adafruit_BMP085.h>
#include <MPU6500_WE.h>
#define MPU6500_ADDR 0x68

Adafruit_BMP085 bmp;
MPU6500_WE myMPU6500 = MPU6500_WE(MPU6500_ADDR);

unsigned long timeReal = 0;
float dataPacket[7];

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
  radio.openWritingPipe(address);
  

  // ************************
  // MPU6500
  if(!myMPU6500.init()){
    Serial.println("MPU6500 not working");
  }
  else{
    Serial.println("MPU6500 is on");
  }
  
  Serial.println("Calibrating MPU6500...");
  myMPU6500.autoOffsets();  // MPU6500 autocalibration
  delay(1000);
  
  Serial.println("MPU6500 is ready");
  
  myMPU6500.enableGyrDLPF();  // Digital Low Pass Filter activated
  myMPU6500.setGyrDLPF(MPU6500_DLPF_6);  // Less noise mode
  myMPU6500.setSampleRateDivider(5);   
  myMPU6500.setGyrRange(MPU6500_GYRO_RANGE_250);
  myMPU6500.setAccRange(MPU6500_ACC_RANGE_2G);
  myMPU6500.enableAccDLPF(true);  // Digital Low Pass Filter activated
  myMPU6500.setAccDLPF(MPU6500_DLPF_6);  // Less noise mode
  

  // ************************
  // BMP 180
  // Initialize the sensor (it is important to get calibration values stored on the device).
  if (!bmp.begin()){
    Serial.println("BMP180 not working");
    while(1); // Pause forever.
  }
  delay(1000);
  
  Serial.println("");
  Serial.println("AHORA SI, PAL BUNKER QUE NOS FUIMOS");  // Everything is ready
  Serial.println("");
}

// =============

void loop()
{
  float temp,pres,alt;
  int verif = 0;
  
  // BMP 180
  temp = bmp.readTemperature();
  pres = bmp.readPressure();
  alt = bmp.readAltitude();
    
  // MPU6500
  xyzFloat gValue = myMPU6500.getGValues();
  xyzFloat gyr = myMPU6500.getGyrValues();
  // float resultantG = myMPU6500.getResultantG(gValue);  // Resultante de G


  // PACKET1
  dataPacket[0] = verif;
  dataPacket[1] = alt;
  dataPacket[2] = pres/100;
  dataPacket[3] = temp;

  // Sending PACKET1 to receptor
  radio.write(&dataPacket, sizeof(dataPacket));

  // PACKET2
  verif = 1;
  dataPacket[0] = verif;
  dataPacket[1] = gValue.x;
  dataPacket[2] = gValue.y;
  dataPacket[3] = gValue.z;
  dataPacket[4] = gyr.x;
  dataPacket[5] = gyr.y;
  dataPacket[6] = gyr.z;

  // Sending PACKET2 to receptor
  radio.write(&dataPacket, sizeof(dataPacket));
}