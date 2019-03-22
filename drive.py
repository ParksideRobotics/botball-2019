#!/usr/bin/python
try:
	import wallaby as w
except ImportError:
	import imp; w = imp.load_source('wallaby', '/home/travis/build/ParksideRobotics/botball-2019/libwallaby/lib/')
import const as c

RIGHT_TURN = 0
LEFT_TURN = 1

def stop():
	"""Turns off both drive motors"""
	c.leftMotor.off()
	c.rightMotor.off()

def freeze():
	"""Freezes both drive motors"""
	c.leftMotor.motor(0)
	c.rightMotor.motor(0)

def driveMotor(left, right, tick):
	"""Uses ticks to move motors"""
	c.leftMotor.clearPositionCounter()
	c.rightMotor.clearPositionCounter()
	c.leftMotor.motor(left)
	c.rightMotor.motor(int(right*c.motorScale))
	while abs(w.gmpc(c.leftMotor.port())) < abs(tick) or abs(w.gmpc(c.rightMotor.port())) < abs(tick):
		continue
	c.leftMotor.off()
	c.rightMotor.off()

def forward(speed, tick):
	"""Moves robot forward at a speed, and for a certain number of ticks"""
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
	while abs(w.gmpc(c.leftMotor.port())) < abs(c.DRIVE_DEG2TICK(degree)) or abs(w.gmpc(c.rightMotor.port())) < abs(c.DRIVE_DEG2TICK(degree)):
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

def driveMotorA(left, right):
	"""DRIVE MOTOR THAT ONLY TURNS ON MOTORS"""
	if left != 0:
		c.leftMotor.motor(left)
	if right != 0:
		c.rightMotor.motor(right)
	
def skipLine(speed, sensor, line, lines):
	"""Speed: How fast we want to go\n
	Sensor: Which tophat to use\n
	Line: Which line to use\n
	Lines: how many we want to skip"""
	for i in range(0, lines):
		while w.analog(sensor) > line: # is on line
			drive_noblock(speed)
		while w.analog(sensor) < line: # isnt on line
			drive_noblock(speed)
	stop()

def turnUntilLine(speed, direction, sensor, line):
	if direction:
		driveMotorA(speed*-1, speed)
	else:
		driveMotorA(speed, speed*-1)
	while w.analog(sensor) > line: # not on line
		continue
	freeze()
	stop()
