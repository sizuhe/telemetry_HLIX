import serial.tools.list_ports
import matplotlib.pyplot as plt


print("Empezando a tomar datos del Don Ardui...")

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = "COM4"    # Puerto donde esta conectado el Arduino Uno
serialInst.open()

matrix = True
tiempoFinal = 0     # TIMEOUT
tiempo = 0
ltiempo = []
lalti = []
lpres= []
ltemp = []
lacelx = []
lacely = []
lacelz = []
lgirx = []
lgiry = []
lgirz = []
laltu = []

while matrix == True:    
    if serialInst.in_waiting:
        tiempoFinal = 0
        pos = 0
        
        # Leer y decodificar la informacion del puerto serial
        packet = serialInst.readline()
        packet = packet.decode("utf")
        packet = packet.split(',')
        
        # Tiempo durante el cual se han tomado datos
        print(f"Tiempo: {tiempo} s")
        ltiempo.append(tiempo)

        # Se agregan los datos a las variables respectivas
        lalti.append(float(packet[0]))
        lpres.append(float(packet[1]))
        ltemp.append(float(packet[2]))
        lacelx.append(float(packet[3]))
        lacely.append(float(packet[4]))
        lacelz.append(float(packet[5]))
        lgirx.append(float(packet[6]))
        lgiry.append(float(packet[7]))
        lgirz.append(float(packet[8]))

        # Tiempo (segundos) durante el cual se tomaran datos
        if tiempo == 30:
            break
        
        # Agregar medio segundo al contador
        tiempo += 0.5
    
    # En caso de que haya un error en la toma de datos - TIMEOUT DE COMUNICACION
    # Si se dejan de recibir datos al puerto serial por alrededor de 30 segundos
    # se corta el programa y se guardan los datos obtenidos hasta el momento
    while serialInst.in_waiting == 0:
        tiempoFinal += 1
        if tiempoFinal >= 4000000:
            print("Mor, hubo un error asi que vamos a acabar el proceso de toma de datos")
            tiempoFinal = 0
            matrix = False
            break
                 
print("Papi, finalizamos la toma de datos")

# Promedios de los datos
promtemp = round(sum(ltemp)/len(ltemp),2)
prompres = round(sum(lpres)/len(lpres),2)
promalti = round(sum(lalti)/len(lalti),2)

# Para calcular la altura
alt0 = (lalti[0]+lalti[1]+lalti[2])/3   # "Calibracion" de la altura inicial
for altitudMedida in lalti:
    altura = round(altitudMedida - alt0,2)
    laltu.append(altura)
promaltu = round(sum(laltu)/len(laltu),2)


# GRAFICAS
plt.plot(ltiempo,lalti)
plt.axhline(y=promalti,color="r")
plt.title("Altitud durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Altitud [m]")
plt.tight_layout()
plt.savefig("Grafica de altitud.pdf")
plt.show()

plt.plot(ltiempo,laltu)
plt.axhline(y=promaltu,color="r")
plt.title("Altura durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Altura [m]")
plt.tight_layout()
plt.savefig("Grafica de altura.pdf")
plt.show()

plt.plot(ltiempo,lpres)
plt.axhline(y=prompres,color="r")
plt.title("Presion atmosferica durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Presion [hPa]")
plt.tight_layout()
plt.savefig("Grafica de presion atmosferica.pdf")
plt.show()

plt.plot(ltiempo,ltemp)
plt.axhline(y=promtemp,color="r")
plt.title("Temperatura durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Temperatura [C]")
plt.tight_layout()
plt.savefig("Grafica de temperatura.pdf")
plt.show()


# Acelerometro
plt.plot(ltiempo,lacelx)
plt.title("Aceleraciones en el eje x durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleracion en eje x [G]")
plt.tight_layout()
plt.savefig("Grafica de acelx.pdf")
plt.show()

plt.plot(ltiempo,lacely)
plt.title("Aceleraciones en el eje y durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleracion en eje y [G]")
plt.tight_layout()
plt.savefig("Grafica de acely.pdf")
plt.show()

plt.plot(ltiempo,lacelz)
plt.title("Aceleraciones en el eje z durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleracion en eje z [G]")
plt.tight_layout()
plt.savefig("Grafica de acelz.pdf")
plt.show()


# Giroscopio
plt.plot(ltiempo,lgirx)
plt.title("Cambios en el angulo del eje x durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Cambio en angulo del eje x [º/s]")
plt.tight_layout()
plt.savefig("Grafica de angux.pdf")
plt.show()

plt.plot(ltiempo,lgiry)
plt.title("Cambios en el angulo del eje y durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Cambio en angulo del eje y [º/s]")
plt.tight_layout()
plt.savefig("Grafica de anguy.pdf")
plt.show()

plt.plot(ltiempo,lgirz)
plt.title("Cambios en el angulo del eje z durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Cambio en angulo del eje z [º/s]")
plt.tight_layout()
plt.savefig("Grafica de anguz.pdf")
plt.show()