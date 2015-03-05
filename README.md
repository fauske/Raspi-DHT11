# Raspi-DHT11
Raspberry Pi with Teensy2.0 and DHT11 sensor

If you have the DHT11 sensor and you want Raspberry Pi to read this data, you might have found out that Raspberry a lot of times is not able to read the data successfully. As far as I know this is due to timing issues. Since I had a Teensy 2.0 board lying around I figured why not use this?

So I found some help online in various forums, and put together this little lines of code.

teensy.c 
tempRead.py

As you may have guessed the teensy.c is what we will program the Teensy 2.0. For this I used Teensyduino. Since Teensyduino only supports Arduino version 1.0.5 and 1.0.6 you will need one of those old versions. 

http://arduino.googlecode.com/files/arduino-1.0.5-r2-windows.zip
https://www.pjrc.com/teensy/td_120/teensyduino.exe

Then just program the Teensy board with the given code in teensy.c And remember, I programmed it with a speed of 8Mhz.

teensy.c
This will program the Teensy to read the data from the DHT11 sensor, but it will only send the readings out via serial IF the Teensy recieve a poll. This is just to keep things a little bit tidy. This poll is just a simple '1'

tempRead.py
This python script will firstly send a poll to the Teensy board in order to get a reading back from Teensy. It will save the readings from the Teensy in a file in /home/pi/temp/YYYY-MM-DD.csv. The format in this file will be something like this
08:19:02,39.00,18.00
This means that it is a comma separated file, with the time the measurement is made first, then the humidity of 39%, lastly the temperature of 18 Celsius.
