from serial import Serial
import time

serialPort = Serial("/dev/ttyACM0", 115200, timeout=1.0)	
if (serialPort.isOpen() == False):
    serialPort.open()
serialPort.flushInput()
serialPort.flushOutput()

while(1==1):
    time.sleep(0.2)
    outStr = raw_input("texto:")
    inStr = ''
    while (inStr is ""):
        serialPort.write(outStr+"\n")
        time.sleep(0.05)
        inStr = serialPort.read(serialPort.inWaiting())

        if(inStr is not ""):
            print "Resultado: {}".format(inStr)
            break
        else:
            print ""
serialPort.close()

