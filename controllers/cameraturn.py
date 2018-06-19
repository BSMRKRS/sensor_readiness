#You have to enter Left or Right twice for it to turn.
#Also, it's caps-sensitive
import setup
import RoboPiLib as RPL
import time as time

#motor pin
mv = 7

#speed
left = 1000
right = 2000

print "Left or Right?"

while True:
    while raw_input("> ") == "Left":
        bro = time.time() + 0.5
        while time.time() < bro:
            RPL.servoWrite(mv, left)
            if time.time() >= bro:
                RPL.servoWrite(mv, 0)
    while raw_input("> ") == "Right":
        bruh = time.time() + 0.5
        while time.time() < bruh:
            RPL.servoWrite(mv, right)
            if time.time() >= bruh:
                RPL.servoWrite(mv, 0)
    else:
        print "Made a mistake there, bud."
