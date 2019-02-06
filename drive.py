#!/usr/bin/python
import wallaby as w
import const as c

def driveMotor(left, right, tick):
	w.cmpc(left)
	w.cmpc(right)
	w.motor(c.leftMotor, int(left*c.motorScale))
	w.motor(c.rightMotor, right)
	while w.gmpc(left) < tick or w.gmpc(right) < tick:
		pass
	w.off(c.leftMotor)
	w.off(c.rightMotor)

def forward(speed, tick):
	driveMotor(speed, speed, tick)

def backward(speed, tick):
	driveMotor(speed*-1, speed*-1, tick)

def spinLeft(speed, tick):
	driveMotor(speed*-1, speed, tick)

def spinRight(speed, tick):
	driveMotor(speed, speed*-1, tick)

def veerLeft(speed, tick, o):
	driveMotor((speed*-1)-o, speed, tick)
	
def veerRight(speed, tick, o):
	driveMotor(speed, (speed*-1)-o, tick)
	
def pivotRight(speed, tick):
	driveMotor(0, speed, tick)

def pivotLeft(speed, tick):
	driveMotor(speed, 0, tick)

def radiusTurn(speed, radius, tick):
	driveMotor(speed, int((radius / (radius+5.0)*speed), tick))

def driveUntilBlack(speed):
	while w.analog(c.largeTopHat) < c.LARGE_TOPHAT_LINE:
		driveMotor(speed, speed, 1)

def lineFollowUntilTape():
	while w.analog(c.smallTopHat) < c.SMALL_TOPHAT_LINE:
		if w.analog(c.largeTopHat) < c.LARGE_TOPHAT_LINE:
			veerLeft(50, 1, 10)
		elif w.analog(c.largeTopHat) > c.LARGE_TOPHAT_LINE:
			veerRight(50, 1, 10)
