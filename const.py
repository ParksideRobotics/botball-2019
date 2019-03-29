#!/usr/bin/python
import wallaby as w

# motors
motorScale = 1
rightMotor = w.Motor(0)
leftMotor = w.Motor(1)
spinner = w.Motor(2)

# servo
camera_servo = w.Servo(0)
collection_arm = w.Servo(1)

# sensors
largeTopHat = w.Analog(0)
smallTopHat = w.Analog(1)
light = w.Analog(2)

# Line
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
last_direction = -1 # default value is -1, left is 0, right is 1

# other shit
# putting shit in const because they are constant
def DRIVE_DEG2TICK(n):
	return n*10.388888888888888888888888888889
def SERVO_TICK2DEG(n):
	return n/11.3777777778
def MOTOR_DEG2TICK(n):
	return n*5.27
