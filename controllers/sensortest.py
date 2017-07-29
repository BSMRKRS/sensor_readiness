import analog_instructions as ana
import time
while True:
    x = ana.forwardtake_reading()
    print x
    time.sleep(0.5)

