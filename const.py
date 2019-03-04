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
largeTopHat = w.Analog(0)
smallTopHat = w.Analog(1)
light = w.Analog(2)
# Line
CREATE_LINE = 2500
LARGE_TOPHAT_LINE = 1800
SMALL_TOPHAT_LINE = 2800

# Color Channels
YELLOW = 0
BURNING = 1
GREEN = 2
RED = 3

# shit for gyro
bias = 0
turn_conversion = 5200

# shit for spinner
distance_traveled = 0

# shit for camera
b = False
burning_center = -1 # default value is -1, Close is 0, far is 1