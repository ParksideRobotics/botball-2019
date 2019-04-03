#!/usr/bin/python
import wallaby as w

# motors\
arm = w.Motor(0)
#servo 

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
light = w.Analog(3)  


# Line
CREATE_GREY = 2500
CREATE_BLACK = 1800
CREATE_WHITE = 2800

# 
ARM_BACK = 666
CLAW_CLOSED = 1250
ARM_FRONT = -600
CLAW_OPENED = 56
  

    