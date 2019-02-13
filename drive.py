#!/usr/bin/python
import wallaby as w
import const as c

def driveMotor(left, right, tick):
	w.cmpc(left)
	w.cmpc(right)
	c.leftMotor.motor(int(left*c.motorScale))
	c.rightMotor.motor(right)
	while w.gmpc(left) < tick or w.gmpc(right) < tick:
		continue
	c.leftMotor.off()
	c.rightMotor.off()

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
	while c.smallTopHat.value() < c.SMALL_TOPHAT_LINE:
		if c.largeTopHat.value() < c.LARGE_TOPHAT_LINE:
			veerLeft(50, 1, 10)
		elif c.largeTopHat.value() > c.LARGE_TOPHAT_LINE:
			veerRight(50, 1, 10)
