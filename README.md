# Hardware
- BMP180
- MPU9250
- nRF24L01+ PA/LNA
- Arduino Uno
- Arduino Nano

**Note:** `_Receptor.ino_` and `Transmitter.ino_` should be uploaded to Arduino Uno and Arduino Nano respectively.


# Configuration
## Transmitter (Arduino Nano)
Takes data measured by BMP180 and MPU9250 and sends it through the nRF24L01+ PA/LNA. Data is divided and sent using two data packets (PACKET1 and PACKET2).

### Connections
| **Arduino Nano** | **BMP180** | **MPU9250** | **nRF24L01+ PA/LNA** |
|:----------------:|:----------:|:-----------:|:--------------------:|
|        GND       |     GND    |     GND     |          GND         |
|        5V        |     VCC    |     VCC     |          VCC         |
|        A4        |     SDA    |     SDA     |           -          |
|        A5        |     SCL    |     SCL     |           -          |
|        D8        |      -     |      -      |          CSN         |
|        D9        |      -     |      -      |          CE          |
|        D11       |      -     |      -      |         MOSI         |
|        D12       |      -     |      -      |         MISO         |
|        D13       |      -     |      -      |          SCK         |

## Receptor (Arduino Uno)
Differentiates incoming data packets and send them through serial communication.

### Connections
| **Arduino Nano** | **nRF24L01+ PA/LNA** |
|:----------------:|:--------------------:|
|        GND       |          GND         |
|        5V        |          VCC         |
|        D8        |          CSN         |
|        D9        |          CE          |
|        D11       |         MOSI         |
|        D12       |         MISO         |
|        D13       |          SCK         |

## Data analysis
`_main.py_` divides incoming serial data by commas, it then graphicates all data.

**Note:** COM port might need to be changed depending on your connections.


# Notes
- Time during which data is taken might be infinite (`timeRead = 0`).
- TIMEOUT time might vary depending on computer used.
