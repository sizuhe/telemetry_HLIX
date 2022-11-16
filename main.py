import serial.tools.list_ports
import matplotlib.pyplot as plt



print("Starting...")

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = "COM4"    # Arduino port
serialInst.open()

matrix = True
timeTIMEOUT = 0
timeRead = 0
timesList = []
altitudeList = []
pressureList= []
temperatureList = []
acelerationxList = []
acelerationyList = []
acelerationzList = []
girxList = []
giryList = []
girzList = []
altitudeList = []

while matrix == True:    
    if serialInst.in_waiting:
        timeTIMEOUT = 0
        pos = 0
        
        # Reading and decoding incoming data
        packet = serialInst.readline()
        packet = packet.decode("utf")
        packet = packet.split(',')
        
        # Time passed since datasave start
        print(f"Time: {timeRead} s")
        timesList.append(timeRead)

        # Adding data to respective variables
        altitudeList.append(float(packet[0]))
        pressureList.append(float(packet[1]))
        temperatureList.append(float(packet[2]))
        acelerationxList.append(float(packet[3]))
        acelerationyList.append(float(packet[4]))
        acelerationzList.append(float(packet[5]))
        girxList.append(float(packet[6]))
        giryList.append(float(packet[7]))
        girzList.append(float(packet[8]))

        # Time duration [seconds] of function
        if timeRead == 30:
            break
        
        # Adding half a second
        timeRead += 0.5
    
    # Communication timeout
    # If data stops coming the function will stop after 30 seconds and data will be saved
    while serialInst.in_waiting == 0:
        timeTIMEOUT += 1
        if timeTIMEOUT >= 4000000:
            print("TIMEOUT - Data reading stopped")
            timeTIMEOUT = 0
            matrix = False
            break
                 
print("Data reading finalized")

# Data averages
temperatureAverage = round(sum(temperatureList)/len(temperatureList),2)
pressureAverage = round(sum(pressureList)/len(pressureList),2)
altitudeAverage = round(sum(altitudeList)/len(altitudeList),2)

# Height calculation
alt0 = (altitudeList[0]+altitudeList[1]+altitudeList[2])/3   # Height "calibration"
for altitudeRead in altitudeList:
    height = round(altitudeRead - alt0,2)
    altitudeList.append(height)
heightAverage = round(sum(altitudeList)/len(altitudeList),2)

# ==============================
# GRAPHS (Spanish)
plt.plot(timesList,altitudeList)
plt.axhline(y=altitudeAverage,color="r")
plt.title("Altitud durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Altitud [m]")
plt.tight_layout()
plt.savefig("Grafica de altitud.pdf")
plt.show()

plt.plot(timesList,altitudeList)
plt.axhline(y=heightAverage,color="r")
plt.title("Altura durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Altura [m]")
plt.tight_layout()
plt.savefig("Grafica de altura.pdf")
plt.show()

plt.plot(timesList,pressureList)
plt.axhline(y=pressureAverage,color="r")
plt.title("Presion atmosferica durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Presion [hPa]")
plt.tight_layout()
plt.savefig("Grafica de presion atmosferica.pdf")
plt.show()

plt.plot(timesList,temperatureList)
plt.axhline(y=temperatureAverage,color="r")
plt.title("Temperatura durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Temperatura [C]")
plt.tight_layout()
plt.savefig("Grafica de temperatura.pdf")
plt.show()


# Accelerometer
plt.plot(timesList,acelerationxList)
plt.title("Aceleraciones en el eje x durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleracion en eje x [G]")
plt.tight_layout()
plt.savefig("Grafica de acelx.pdf")
plt.show()

plt.plot(timesList,acelerationyList)
plt.title("Aceleraciones en el eje y durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleracion en eje y [G]")
plt.tight_layout()
plt.savefig("Grafica de acely.pdf")
plt.show()

plt.plot(timesList,acelerationzList)
plt.title("Aceleraciones en el eje z durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleracion en eje z [G]")
plt.tight_layout()
plt.savefig("Grafica de acelz.pdf")
plt.show()


# Gyroscope
plt.plot(timesList,girxList)
plt.title("Cambios en el angulo del eje x durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Cambio en angulo del eje x [º/s]")
plt.tight_layout()
plt.savefig("Grafica de angux.pdf")
plt.show()

plt.plot(timesList,giryList)
plt.title("Cambios en el angulo del eje y durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Cambio en angulo del eje y [º/s]")
plt.tight_layout()
plt.savefig("Grafica de anguy.pdf")
plt.show()

plt.plot(timesList,girzList)
plt.title("Cambios en el angulo del eje z durante el vuelo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Cambio en angulo del eje z [º/s]")
plt.tight_layout()
plt.savefig("Grafica de anguz.pdf")
plt.show()