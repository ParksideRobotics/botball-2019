#!/usr/bin/python
import wallaby as w
import const as c
import drive as d
import math

max = false

def getGreatest(channel):
	highestconfidence = 0
	greatest = 0
	for i in range(channel, w.get_object_count(channel)):
			if w.get_object_confidence(channel, i) > highestconfidence:
				highestconfidence = w.get_object_confidence(channel, i)
				greatest = i
	return greatest

def centerX(channel, greatest):
	if w.get_object_center_x(channel, greatest) < (w.get_camera_width() / 2.0) - 20:
		c.leftMotor.off()
		c.rightMotor.motor(50)
	elif w.get_object_center_x(channel, greatest) > (w.get_camera_width() / 2.0) + 20:
		c.rightMotor.off()
		c.leftMotor.motor(50)

def centerX_servo(channel, greatest):
	if w.get_object_center_x(channel, greatest) < (w.get_camera_width() / 2.0) - 10:
		w.set_servo_position(0, w.get_servo_position(0)+50)
	elif w.get_object_center_x(channel, greatest) > (w.get_camera_width() / 2.0) + 10:
		w.set_servo_position(0, w.get_servo_position(0)-50)

def scan_servo(channel, last_seen_x):
	if not c.camera_servo.isEnabled():
		c.camera_servo.enable()

	if last_seen_x == -1: # basically go back and forth with our position to scan for an object
		if max:
			c.camera_servo.setPosition(c.camera_servo.position()+1)
		elif not max:
			c.camera_servo.setPostition(c.camera_servo.position()-1)
		elif c.camera_servo.position() == 2047 or c.camera_servo.position() == 0:
			max = not max
	
	# go in the direction that we last saw the cube, so we can find it again
	if last_seen_x < w.get_camera_width()/2:
		c.camera_servo.setPosition(c.camera_servo.position()-1)
	elif last_seen_x > w.get_camera_width()/2:
		c.camera.servo.setPosition(c.camera_servo.position()+1)
		