#!/usr/bin/python
import wallaby as w
import const as c

def driveMotor(left, right, time):
	w.motor(c.leftMotor, int(left*c.motorScale))
	w.motor(c.rightMotor, right)
	if time == 0:
	w.msleep(time)
	w.off(c.leftMotor)
	w.off(c.rightMotor)

def forward(speed, time):
	driveMotor(speed, speed, time)

def backward(speed, time):
	driveMotor(speed*-1, speed*-1, time)

def spinLeft(speed, time):
	driveMotor(speed*-1, speed, time)

def spinRight(speed, time):
	driveMotor(speed, speed*-1, time)

def veerLeft(speed, time, o):
	driveMotor((speed*-1)-o, speed, time)
	
def veerRight(speed, time, o):
	driveMotor(speed, (speed*-1)-o, time)
	
def pivotRight(speed, time):
	driveMotor(0, speed, time)

def pivotLeft(speed, time):
	driveMotor(speed, 0, time)

def radiusTurn(speed, radius, time):
	driveMotor(speed, int((radius / (radius+5.0)*speed), time))

def driveUntilBlack(speed):
	while w.analog(c.largeTopHat) < c.LARGE_TOPHAT_LINE:
		driveMotor(speed, speed, 1)

def lineFollowUntilTape():
	while w.analog(c.smallTopHat) < c.SMALL_TOPHAT_LINE:
		if w.analog(c.largeTopHat) < c.LARGE_TOPHAT_LINE:
			veerLeft(50, 1, 10)
		elif w.analog(c.largeTopHat) > c.LARGE_TOPHAT_LINE:
			veerRight(50, 1, 10)