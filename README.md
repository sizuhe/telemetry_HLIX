# Hardware usado
- BMP180
- MPU9250
- nRF24L01+ PA/LNA
- Arduino Uno
- Arduino Nano

**Nota:** Los archivos "_Receptor.ino_" y "_Transmisor.ino_" se cargan al Arduino Uno y Arduino Nano respectivamente. 

</br>

# Componentes
## Transmisor
Toma los datos medidos por los módulos BMP180 y MPU9250 para luego enviarlos usando el nRF24L01+ PA/LNA. El envío de los datos se hace de forma diferenciada en dos paquetes de datos (PACKET1 y PACKET2).

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
Diferencia los dos paquetes de datos entrantes y los envía por medio de comunicación serial.

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


## Análisis de datos
El archivo "_main.py_" toma los datos entrantes por puerto serial y los separa según el uso de comas (,) para graficarlos posteriormente. 

**Nota:** El puerto COM debe ser el mismo donde se encuentre conectado el Receptor (Arduino Uno), _modificar en código_.

</br>

# Notas
- El tiempo durante el cual se toman datos puede variar, se escribió de esta forma para que el código finalizara correctamente. Sin embargo, este puede ser eliminado (tiempo infinito).
- El tiempo de espera (TIMEOUT) entre la comunicación del Receptor y Transmisor puede depender de la velocidad de procesamiento del computador usado. 
- Si el código es detenido mediante teclado, no se mostrarán gráficas de los datos.
