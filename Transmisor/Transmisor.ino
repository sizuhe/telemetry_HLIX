#include <Wire.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Adafruit_BMP085.h>
#include <MPU6500_WE.h>
#define MPU6500_ADDR 0x68

Adafruit_BMP085 bmp;
MPU6500_WE myMPU6500 = MPU6500_WE(MPU6500_ADDR);

unsigned long tiempoactual = 0;
float datos[7];   // Array con 8 variables
String coma = ",";    // Lit, es una coma

//create an RF24 object
RF24 radio(9, 8);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";

// =============

void setup()
{
  Serial.begin(9600);
  radio.begin();
  
  //set the address
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
  myMPU6500.autoOffsets();  // Autocalibracion de los sensores
  delay(1000);
  
  Serial.println("MPU6500 is ready");
  
  myMPU6500.enableGyrDLPF();  // Digital Low Pass Filter activado
  myMPU6500.setGyrDLPF(MPU6500_DLPF_6);  // Usando nivel 6 de filtro, este es el de menor ruido
  myMPU6500.setSampleRateDivider(5);   
  myMPU6500.setGyrRange(MPU6500_GYRO_RANGE_250);
  myMPU6500.setAccRange(MPU6500_ACC_RANGE_2G);
  myMPU6500.enableAccDLPF(true);  // Digital Low Pass Filter activado
  myMPU6500.setAccDLPF(MPU6500_DLPF_6);  // Usando nivel 6 de filtro, este es el de menor ruido
  
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
  int cont = 0;
  
  // BMP 180
  temp = bmp.readTemperature();
  pres = bmp.readPressure();
  alt = bmp.readAltitude();
    
  // MPU6500
  xyzFloat gValue = myMPU6500.getGValues();
  xyzFloat gyr = myMPU6500.getGyrValues();
  // float resultantG = myMPU6500.getResultantG(gValue);  // En caso de querer el valor de la resultante para G


  // PRIMER PACKET DE DATOS - PACKET1
  datos[0] = verif;
  datos[1] = alt;
  datos[2] = pres/100;
  datos[3] = temp;

  // // Mostrando los datos cada segundo (FOR DEBUG)
  // if (millis() - tiempoactual >= 1000){
  //   Serial.println("--------------------");
  //   Serial.println(verif);
  //   Serial.print("Altitud [m]: ");
  //   Serial.println(datos[1]);
  //   Serial.print("Presion atmosferica [hPa]: ");
  //   Serial.println(datos[2]);
  //   Serial.print("Temperatura [ºC]: ");
  //   Serial.println(datos[3]);
  //   cont = 1;
  //   tiempoactual = millis();
  // }

  // Enviando los datos al receptor
  radio.write(&datos, sizeof(datos));


  // SEGUNDO PACKET DE DATOS - PACKET2
  verif = 1;
  datos[0] = verif;
  datos[1] = gValue.x;
  datos[2] = gValue.y;
  datos[3] = gValue.z;
  datos[4] = gyr.x;
  datos[5] = gyr.y;
  datos[6] = gyr.z;

  // Enviando los datos al receptor
  radio.write(&datos, sizeof(datos));

  // // Mostrando los datos cada segundo (FOR DEBUG)
  // if (cont == 1){
  //   Serial.println(verif);
  //   Serial.print("Aceleración (x,y,z) [G]: ");
  //   Serial.println(datos[1] + coma + datos[2] + coma + datos[3]);
  //   Serial.print("Giroscopio [º/s]: ");
  //   Serial.println(datos[4] + coma + datos[5] + coma + datos[6]);
  // }
}