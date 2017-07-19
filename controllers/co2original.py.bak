import serial
import time
ser = serial.Serial("/dev/ttyAMA0",9600)
print "Serial Connected!"
ser.write("K 2\r\n")
ser.flushInput()
time.sleep(1)
while True:
    ser.write("Z\r\n")
    time.sleep(.01)
    resp = ser.read(10)
    resp = resp[:8]
    print " "
    print " "
    fltCo2 = float(resp[2:])
    if fltCo2 >= 400:
        print "Life!"
        print "Co2 = " + str(fltCo2) + " PPM"
    else:
        print "no life detected"
    time.sleep(1)
