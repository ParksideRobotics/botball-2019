#!/usr/bin/python
import os, sys
from wallaby import *

# Globals
leftMotor = Motor(1)
rightMotor = Motor(0)
topHat = Analog(0)
rangeFinder = Analog(1)
pushSensor = Digital(0)
claw = Servo(0)

def Drive(power):
	leftMotor.motorPower(power)
	rightMotor.motorPower(power)

def Turn(power, radius):
	leftMotor.motorPower(power)
	rightMotorPower = int((radius / (radius + 5.0))*power)
	print rightMotorPower
	rightMotor.motorPower(rightMotorPower)

def main():
	print "Hello World"

	print "Tophat: %d" % topHat.value(),
	print "Rangefinder: %d" % rangeFinder.value(),
	print "PushSensor %d" % pushSensor.value()

	while True:
		Turn(100, int(sys.argv[1]))

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()
