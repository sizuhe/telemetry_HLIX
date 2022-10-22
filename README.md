# Hardware usado
- BMP180
- MPU9250
- nRF24L01+ PA/LNA
- Arduino Uno
- Arduino Nano

**Nota:** Los archivos "_Receptor.ino_" y "_Transmisor.ino_" se cargan al Arduino Uno y Arduino Nano respectivamente. 

---
# Componentes
## Transmisor
Toma los datos medidos por los modulos BMP180 y MPU9250 para luego enviarlos usando el nRF24L01+ PA/LNA. El envio de los datos se hace de forma diferenciada en dos paquetes de datos (PACKET1 y PACKET2).

### Conexiones
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


## Receptor
Diferencia los dos paquetes de datos entrantes y los envia por medio de comunicacion serial.

### Conexiones
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


## Analisis de datos
El archivo "_Analisis de datos.py_" toma los datos entrantes por puerto serial y los separa segun el uso de comas (,) para graficarlos posteriormente. 

**Nota:** El puerto COM debe ser el mismo donde se encuentre conectado el Receptor (Arduino Uno) - **_modificar en codigo_**.

---

# Notas
- El tiempo durante el cual se toman datos puede variar, se escribio de esta forma para que el codigo finalizara correctamente. Sin embargo, este puede ser eliminado (tiempo infinito).
- El tiempo de espera (TIMEOUT) entre la comunicacion del Receptor y Transmisor puede depender de la velocidad de procesamiento del computador usado. 
- Si el codigo es detenido mediante teclado no se mostraran graficas de los datos.
