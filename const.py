#!/usr/bin/python
import wallaby as w

# motors\

#servo 
arm = w.Servo(0) # just put this in for testing
claw = w.Servo(1) # just putting this in for testing
# sensors
largeTopHat = 0
rangeFinder = 1
smallTopHat = 2
pushButton = 0


pushButton = w.Digital(0)
largeTopHat = w.Analog(0)
rangeFinder = w.Analog(1)
smallTopHat = w.Analog(2)
light = w.Analog(3)  # Not actually on robot yet


# Line
CREATE_GREY = 2500
CREATE_BLACK = 1800
CREATE_WHITE = 2800

# servos
ARM = 1600
CLAW = 0
  

    