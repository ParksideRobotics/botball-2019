#!/usr/bin/python
import wallaby as w
import const as c

def stop():
	w.create_stop()

def driveMotor(left, right, tick):
	w.create_drive_direct(left, right)
	w.msleep(time)
	w.create_stop()

def forward(speed, time):
	w.create_drive_straight(speed)
	w.msleep(time)
	w.create_stop()

def backward(speed, time):
	w.create_drive_straight(speed*-1)
	w.msleep(time)
	w.create_stop()

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
	while w.get_lfcliff_amt() < c.CREATE_LINE:
		w.create_drive_straight(speed)

def driveUntilWhite(speed):
	while w.get_lfcliff_amt() > c.CREATE_LINE:
		w.create_drive_straight(speed)

def lineFollowUntilTape():
	while w.get_lfcliff_amt() < c.CREATE_LINE
		if w.get_rfcliff_amt() < c.CREATE_LINE:
			veerLeft(50, 1, 10)
		elif w.get_rcliff_amt() > c.CREATE_LINE:
			veerRight(50, 1, 10)

def degreeTurn(speed, degree): 
	w.create_spin_block(speed, degree)
