#!/usr/bin/python
import wallaby as w
import const as c

def stop():
	w.create_stop()

def driveMotor(left, right, time):
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

def spinLeft(speed, time):
	driveMotor(speed*-1, speed, time)

def spinRight(speed, time):
	driveMotor(speed, speed*-1, time)

def veerLeft(speed, time, o):
	driveMotor((speed*-1)-o, speed, time)
	
def veerRight(speed, time, o):
	driveMotor(speed, (speed*-1)-o, time)
	
def pivotLeft(speed, time):
	driveMotor(0, speed, time)

def pivotRight(speed, time):
	driveMotor(speed, 0, time)

def radiusTurn(speed, radius, time):
	driveMotor(speed, int((radius / (radius+5.0)*speed), time))

def driveUntilBlack(speed):
	while w.get_create_lfcliff_amt() > c.CREATE_LINE:
		w.create_drive_straight(speed)

def driveUntilWhite(speed):
	while w.get_create_lfcliff_amt() < c.CREATE_LINE:
		w.create_drive_straight(speed)

def lineFollowUntilTape():
	while w.get_create_lfcliff_amt() < c.CREATE_LINE:
		if w.get_create_rfcliff_amt() < c.CREATE_LINE:
			veerLeft(50, 1, 10)
		elif w.get_create_rcliff_amt() > c.CREATE_LINE:
			veerRight(50, 1, 10)

def degreeTurn(speed, degree): 
	w.create_spin_block(speed, degree)
