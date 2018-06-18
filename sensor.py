#this code is good if the analog sensors are set up to measure the blind spots
# of the camera
import RoboPiLib as RPL
import setup
import time

#setting up pins for analog sensors
left =
rf =
rb =

while True:
    while RPL.analogRead(rf) >= 400:
        print " - "
    while RPL.analogRead(rf) < 400:
        print "something in front right"
    while RPL.analogRead(left) >= 400:
        print " - "
    while RPL.analogRead(left) < 400:
        print "something to the left"
    while RPL.analogRead(rb) >= 400:
        print " - "
    while RPL.analogRead(rb) < 400:
        print "something in back right"
