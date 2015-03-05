#!/usr/bin/python

import serial, time, datetime
ser = serial.Serial('/dev/ttyACM0',  9600, timeout = 0.1)
now = datetime.datetime.now()

def send_and_receive( theinput ):
  ser.write( theinput )
  while True:
    try:
      time.sleep(0.01)
      state = ser.readline()
      #print state
      return state
    except:
      pass
  time.sleep(0.1)

filnavn = '/home/pi/temp/'+str(now.date())+'.csv'

f = open(filnavn,'a')
test = True;

while test :
    arduino_sensor = send_and_receive('1')
    T = now.strftime("%H:%M:%S,")
    if arduino_sensor:
	f.write(T)
    	f.write(arduino_sensor)
    	f.close()
    	f = open(filnavn,'a')
    	test = False;
    else:
	test = True;
