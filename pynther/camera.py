#!/usr/bin/python
import wallaby as w
import const as c
import drive as d
import math
import sys

def getGreatest(channel):
	highestconfidence = 0
	greatest = 0
	for i in range(0, w.get_object_count(channel)):
			if w.get_object_confidence(channel, i) > highestconfidence:
				highestconfidence = w.get_object_confidence(channel, i)
				greatest = i
	return greatest

def centerX(channel, greatest):
	if w.get_object_center_x(channel, greatest) > (w.get_camera_width() / 2.0) - 5:
		c.leftMotor.motor(10)
		c.rightMotor.motor(30)
		print w.get_object_center_x(channel, greatest),
		print "Turning left!"
	elif w.get_object_center_x(channel, greatest) < (w.get_camera_width() / 2.0) + 5:
		c.rightMotor.motor(10)
		c.leftMotor.motor(30)
		print w.get_object_center_x(channel, greatest),
		print "Turning right!"

def centerX_servo(channel, greatest, tolerance, speed): # we can change tolerance
	if w.get_object_center_x(channel, greatest) < (w.get_camera_width() / 2.0) - tolerance:
		w.set_servo_position(0, w.get_servo_position(0)+speed)
	elif w.get_object_center_x(channel, greatest) > (w.get_camera_width() / 2.0) + tolerance:
		w.set_servo_position(0, w.get_servo_position(0)-speed)

def scan_servo(channel, last_seen_x):
	if not c.camera_servo.isEnabled():
		c.camera_servo.enable()

	if last_seen_x == -1: # basically go back and forth with our position to scan for an object
		if c.b:
			c.camera_servo.setPosition(c.camera_servo.position()+1)
		elif not c.b:
			c.camera_servo.setPosition(c.camera_servo.position()-1)
		elif c.camera_servo.position() == 2047 or c.camera_servo.position() == 0:
			c.b = not c.b
	
	# go in the direction that we last saw the cube, so we can find it again
	if last_seen_x < w.get_camera_width()/2:
		c.camera_servo.setPosition(c.camera_servo.position()-1)
	elif last_seen_x > w.get_camera_width()/2:
		c.camera.servo.setPosition(c.camera_servo.position()+1)
