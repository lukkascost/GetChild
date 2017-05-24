#!/usr/bin/env python         
import time
import serial
ser = serial.Serial(port='/dev/serial0',
               baudrate =9600 ,
               parity=serial.PARITY_NONE,
               timeout=1)
counter=0
while 1:
	print counter
	ser.write("AT+NAME?")
	time.sleep(1)
	counter += 1