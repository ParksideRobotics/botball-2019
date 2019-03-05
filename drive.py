#!/usr/bin/python
import wallaby as w
import const as c

def stop():
	c.leftMotor.off()
	c.rightMotor.off()

def freeze():
	c.leftMotor.motor(0)
	c.rightMotor.motor(0)

def driveMotor(left, right, tick):
	c.leftMotor.clearPositionCounter()
	c.rightMotor.clearPositionCounter()
	c.leftMotor.motor(left)
	c.rightMotor.motor(int(right*c.motorScale))
	while w.gmpc(c.leftMotor.port()) < tick or w.gmpc(c.rightMotor.port()) < tick:
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

def degreeTurn(speed, degree): # had to make custom drive because driveMotor() didn't suit my needs
	"""Turn robot at n speed, and x degrees"""
	w.cmpc(c.leftMotor.port())
	w.cmpc(c.rightMotor.port())
	if degree < 0:
		c.leftMotor.motor(speed*-1)
		c.rightMotor.motor(int(speed*c.motorScale))
	else:
		c.leftMotor.motor(speed)
		c.rightMotor.motor(int(speed*c.motorScale)*-1)
	while abs(w.gmpc(c.leftMotor.port())) < abs(degree*10.388888888888888888888888888889) or abs(w.gmpc(c.rightMotor.port())) < abs(degree*10.388888888888888888888888888889):
		print w.gmpc(c.leftMotor.port()),
		print w.gmpc(c.rightMotor.port())
		continue
	print "Done turning!"
	c.leftMotor.motor(0)
	c.rightMotor.motor(0)
	c.leftMotor.off()
	c.rightMotor.off()

def drive_noblock(speed):
	"""Only turns on drive motors. Does not stop them."""
	c.leftMotor.motor(int(speed*c.motorScale))
	c.rightMotor.motor(speed)