#!/usr/bin/python
import wallaby as w

# motors
motorScale = 1
rightMotor = w.Motor(0)
leftMotor = w.Motor(1)
spinner = w.Motor(2) 

# servo
camera_servo = w.Servo(0)

# sensors
largeTopHat = 0
rangeFinder = 1
smallTopHat = 2
pushButton = 0


pushButton = w.Digital(0)
largeTopHat = w.Analog(0)
rangeFinder = w.Analog(1)
smallTopHat = w.Analog(2)
light = w.Analog(3) # Not actually on robot yet

# Line
CREATE_LINE = 2500
LARGE_TOPHAT_LINE = 1800
SMALL_TOPHAT_LINE = 2800

# Color Channels
YELLOW = 0
GREEN = 1
RED = 2

# shit for gyro
bias = 0
turn_conversion = 5200

# shit for spinner
distance_traveled = 0

# shit for camera
b = False