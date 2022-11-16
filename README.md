# Hardware
- BMP180
- MPU9250
- nRF24L01+ PA/LNA
- Arduino Uno
- Arduino Nano

**Note:** `_Receptor.ino_` and `Transmitter.ino_` should be uploaded to Arduino Uno and Arduino Nano respectively.

</br>

# Components
## Transmitter (Arduino Nano)
Takes data measured by BMP180 and MPU9250 and sends it through the nRF24L01+ PA/LNA. Data is divided and sent using two data packets (PACKET1 and PACKET2).

### Connections
| Arduino Nano | BMP180 | MPU9250 | nRF24L01+ PA/LNA |
|---|---|---|---|
| Ground | GND | GND | GND |
| 5V | VCC | VCC | VCC |
| A4 | SDA | SDA | - |
| A5 | SCL | SCL | - |
| D9 | - | - | CE |
| D8 | - | - | CSN |
| D13 | - | - | SCK |
| D11 | - | - | MOSI |
| D12 | - | - | MISO |
| - | - | - | IRQ |


## Receptor (Arduino Uno)
Differentiates incoming data packets and send them through serial communication.

### Connections
| Arduino Uno | nRF24L01+ PA/LNA |
|---|---|
| Ground | GND |
| 5V | VCC |
| D9 | CE |
| D8 | CSN |
| D13 | SCK |
| D11 | MOSI |
| D12 | MISO |
| - | IRQ |


## Data analysis
`_main.py_` divides incoming serial data by commas, it then graphicates all data.

**Note:** COM port might need to be changed depending on your connections.

</br>

# Notes
- Time during which data is taken might be infinite (`timeRead = 0`).
- TIMEOUT time might vary depending on computer used.