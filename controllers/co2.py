#import serial
#import time
#ser = serial.Serial("/dev/ttyAMA0",9600)
#ser.write("K 2\r\n")
#ser.flushInput()
def co2():
    #ser.write("Z\r\n")
    #time.sleep(.01)
    #resp = ser.read(10)
    #resp = resp[:8]
    #fltCO2 = float(resp[2:])
    #return dict(message=fltCO2,resp=resp)
#def index(): return dict(message="cozir.py")

    import serial
    import time
    ser = serial.Serial("/dev/ttyAMA0",9600)
    ser.write("K 2\r\n")
    ser.flushInput()
    time.sleep(1)
    ser.write("Z\r\n")
    time.sleep(.01)
    resp = ser.read(10).lstrip()
    fst=resp[0]
    tries = 0
    while((tries < 20) and (fst != 'Z')):
        resp = ser.read(10).lstrip()
        fst=resp[0]
        tries = tries + 1
    fltCO2 = float(resp[2:])
    return response.json(dict(message=fltCO2))