# -*- coding: cp1252 -*-
from Classes import *
measurements = [] 
potencias = [-x for x in range(1,110) ]
pl0 = [ -x for x in potencias]
pd0 = 6
n = 2.935
def distanciaPotenciaSinal(potencias, qtd, pd0, n):
    res = []
    for i in range (0, qtd):
        expoente = ((pd0-potencias[i])/(10*n))
        distance = pow(10, expoente)
        mts = distance/100
        res.append(mts)
    return res
distances = distanciaPotenciaSinal(potencias, len(potencias),pd0, n)

serialPort = Serial("/dev/ttyAMA0", 9600, timeout=2.0)	
if (serialPort.isOpen() == False):
    serialPort.open()
serialPort.flushInput()
serialPort.flushOutput()

signal  = 0
while(signal<1000):
    if signal>0:print (measurements[signal-1], distanceOfSignalPower(measurements[signal-1],n=n))
    lista = []
#    time.sleep(1)
    outStr = "AT+RSSI?"
    inStr = ''
    while (inStr is ""):
        serialPort.write(outStr)
        time.sleep(0.05)
        inStr = serialPort.read(serialPort.inWaiting())

        if(inStr is not ""):
            signal += 1
            for h,i in enumerate(inStr):
                if i.isdigit() and h not in lista:
                    lista.append(h)
                    lista.append(h+1)
            break
        else:
            print ""
    valores = []
    for i in range(0,len(lista),2):
        valores.append(int(inStr[lista[i]])*10+int(inStr[lista[i+1]]))
    [measurements.append(x) for x in valores]

serialPort.close()

arquivo = open("Samples/Measurements/One_To_One/Suspend/0500cm.txt", mode='w')
for i in measurements:
    arquivo.write(str(i))
    arquivo.write("\n")
arquivo.close()
