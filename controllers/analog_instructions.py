import RoboPiLib as RoboPi
import time as time
import math #allow for the exponential function
RoboPi.RoboPiInit("/dev/ttyAMA0", 115200)
#AMA0 has a zero

def forwardtake_reading():
    reading_collection = []
    
    reading_volts =  (RoboPi.analogRead(0))

    reading_cm= reading_volts * 1000 / 3.2
    reading_collection = reading_collection.append(reading_cm)

    reading_avg = 0
    if reading_collection == True:
        for input in range(0, 8):
            reading_avg = reading_avg + reading_collection.pop(0)

    reading_avg /= 8

    #return int(reading_avg)
    return reading_volts

