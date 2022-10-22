import serial.tools.list_ports
import matplotlib as plt


print("Empezando a tomar datos del Don Ardui...")

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = "COM3"    # Puerto donde esta conectado el Arduino Uno.
serialInst.open()

matrix = True
tiempoFinal = 0
tiempo = 0      # Segundos
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
        
        # Tiempo durante el cual se han tomado datos
        print(f"Tiempo: {tiempo} s")
        ltiempo.append(tiempo)

        # Guardar en una lista los valores anteriores a una coma encontrada en la cadena de datos
        contador = 0
        
        # Diferenciar por comas los datos entrantes del puerto serial
        for i,j in enumerate(packet):      
            if j == ",":                
                contador += 1
                dato = float(packet[pos:i])
                dato = round(dato,2)
                pos = i+1
                
                # Guardar el dato en la lista respectiva
                if contador == 1:
                    lalti.append(dato)
                elif contador == 2:
                    lpres.append(dato)
                elif contador == 3:
                    ltemp.append(dato)
                elif contador == 4:
                    lacelx.append(dato)
                elif contador == 5:
                    lacely.append(dato)
                elif contador == 6:
                    lacelz.append(dato)
                elif contador == 7:
                    lgirx.append(dato)
                elif contador == 8:
                    lgiry.append(dato)
                elif contador == 9:
                    lgirz.append(dato)
             
        # Tiempo durante el cual se tomaran datos
        # 5 min = 300 s
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
plt.pyplot.plot(ltiempo,lalti)
plt.pyplot.axhline(y=promalti,color="r")
plt.pyplot.title("Altitud durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Altitud [m]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de altitud.pdf")
plt.pyplot.show()

plt.pyplot.plot(ltiempo,laltu)
plt.pyplot.axhline(y=promaltu,color="r")
plt.pyplot.title("Altura durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Altura [m]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de altura.pdf")
plt.pyplot.show()

plt.pyplot.plot(ltiempo,lpres)
plt.pyplot.axhline(y=prompres,color="r")
plt.pyplot.title("Presion atmosferica durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Presion [hPa]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de presion atmosferica.pdf")
plt.pyplot.show()

plt.pyplot.plot(ltiempo,ltemp)
plt.pyplot.axhline(y=promtemp,color="r")
plt.pyplot.title("Temperatura durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Temperatura [C]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de temperatura.pdf")
plt.pyplot.show()


# Acelerometro
plt.pyplot.plot(ltiempo,lacelx)
plt.pyplot.title("Aceleraciones en el eje x durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Aceleracion en eje x [G]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de acelx.pdf")
plt.pyplot.show()

plt.pyplot.plot(ltiempo,lacely)
plt.pyplot.title("Aceleraciones en el eje y durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Aceleracion en eje y [G]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de acely.pdf")
plt.pyplot.show()

plt.pyplot.plot(ltiempo,lacelz)
plt.pyplot.title("Aceleraciones en el eje z durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Aceleracion en eje z [G]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de acelz.pdf")
plt.pyplot.show()


# Giroscopio
plt.pyplot.plot(ltiempo,lgirx)
plt.pyplot.title("Cambios en el angulo del eje x durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Cambio en angulo del eje x [º/s]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de angux.pdf")
plt.pyplot.show()

plt.pyplot.plot(ltiempo,lgiry)
plt.pyplot.title("Cambios en el angulo del eje y durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Cambio en angulo del eje y [º/s]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de anguy.pdf")
plt.pyplot.show()

plt.pyplot.plot(ltiempo,lgirz)
plt.pyplot.title("Cambios en el angulo del eje z durante el vuelo")
plt.pyplot.xlabel("Tiempo [s]")
plt.pyplot.ylabel("Cambio en angulo del eje z [º/s]")
plt.pyplot.tight_layout()
plt.pyplot.savefig("Grafica de anguz.pdf")
plt.pyplot.show()