#!/usr/bin/python
import math
import sys

import camera as x
import const as c
import drive as d
import utilities as u
import wallaby as w

def move_out_startbox():
	c.camera_servo.enable()
	c.camera_servo.setPosition(1500) # set the servo so It can see both centers, but not cubes
	c.collection_arm.setPosition(270) # set the arm to so it is open
	d.forward(50, 650)
	d.spinLeft(50, 100)

def find_burning_center():
	if not w.camera_open():
		return
	while c.burning_center == -1:
		w.camera_update()
		best = x.getGreatest(c.BURNING)
		if w.get_object_confidence(c.BURNING, best) < 0.5:
			continue
		x_pos = w.get_object_center_x(c.BURNING, best)
		print x_pos
		if 0 < x_pos < 59:
			print "Close medical center"
			c.burning_center = 0
			break
		elif 60 < x_pos < 120:
			print "Far medical center"
			c.burning_center = 1
			break
	w.camera_close()

def turn_to_cubes():
	if not w.camera_open():
		return
	servo_centered = False
	c.camera_servo.enable()
	last_seen_x = -1 # setting default value for last seen x
	while not servo_centered: # first center the 
		w.camera_update()
		objects = w.get_object_count(c.YELLOW)
		if objects == 0:
			print "no objects!"
			c.camera_servo.setPosition(2047)
			continue
		best = x.getGreatest(c.YELLOW)
		if w.get_object_confidence(c.YELLOW, best) < 0.5:
			continue
		print "Cube:",
		print w.get_object_center_x(c.YELLOW, best),
		print w.get_object_confidence(c.YELLOW, best)
		last_seen_x = w.get_object_center_x(c.YELLOW, best) # update our last seen before we center to it, in case we move too much
		x.centerX_servo(c.YELLOW, best, 10, 50) # first find it with our servo
		if (w.get_camera_width()/2)-25 < w.get_object_center_x(c.YELLOW, best) < (w.get_camera_width()/2)+10:
			servo_centered = True
			break
	servo_pos = c.camera_servo.position()
	print servo_pos
	print c.SERVO_TICK2DEG(servo_pos)
	print int(c.SERVO_TICK2DEG(servo_pos))
	print int((c.SERVO_TICK2DEG(servo_pos)) - 90)
	d.forward(50, 2100)
	d.stop()
	w.msleep(250)
	d.degreeTurn(50, int(c.SERVO_TICK2DEG(servo_pos) - 75))
	c.camera_servo.setPosition(900) # reset camera to default position
	u.moveDegree(c.spinner.port(), 50, 90) # set our sweeper to default pos
	c.distance_traveled = 0  # clear distance
	w.camera_close()

def move_to_cubes():
	c.camera_servo.setPosition(900)
	d.forward(50, 500)
	w.msleep(250)
	d.degreeTurn(50, 75)
	u.moveDegree(c.spinner.port(), 50, 90)
	c.distance_traveled = 0 # reset distance
	if not w.camera_open():
		return
	at_cubes = False
	ol = -1
	while not at_cubes:
		w.camera_update()
		objects = w.get_object_count(c.YELLOW)
		if objects == 0:
			print "no objects!"
			if ol == 2:
				d.forward(50, 100)
				w.ao()
				at_cubes = True
				print "No objects, but passed line!"
				break
			continue
		best = x.getGreatest(c.YELLOW)
		x.centerX(c.YELLOW, best)
		print ol,
		if u.isOnLine(c.largeTopHat.port(), c.LARGE_TOPHAT_LINE) and ol == -1:
			ol += 1
			print "Hitting first line"
		elif not u.isOnLine(c.largeTopHat.port(), c.LARGE_TOPHAT_LINE) and ol == 0:
			ol += 1
			print "Passed First line"
		elif u.isOnLine(c.largeTopHat.port(), c.LARGE_TOPHAT_LINE) and ol == 1:
			d.stop()
			c.collection_arm.setPosition(1600)
			w.msleep(500)
			c.collection_arm.setPosition(270)
			w.msleep(500)
			ol += 1
			print "Hitting second line"
		elif not u.isOnLine(c.largeTopHat.port(), c.LARGE_TOPHAT_LINE) and ol == 2:
			w.ao()
			at_cubes = True
			print "Passed second line"
			break
		print "Cube:",
		print w.get_object_center_x(c.YELLOW, best),
		print w.get_object_confidence(c.YELLOW, best)
	w.camera_close()

def get_cubes_num(num): # scalable function for getting cubes :))
	degree = 120 # our starting degree for the turn
	for i in range(num):
		if i % 2 == 0:
			u.moveDegree(c.spinner.port(), 50, degree*.8)
			u.resetPosition()
			print "FORWARD %d degrees on cube %d" % (degree*.8, i)
		elif i % 2 == 1:
			u.moveDegree(c.spinner.port(), 50, -degree)
			u.resetPosition()
			print "BACKWARD %d degrees on cube %d" % (degree*.9, i)
		degree -= 20

def move_to_med(): # move to medical center
	print "Moving towards the %s medical center" % (("close", "far")[c.burning_center])
	d.degreeTurn(50, ((-80,-70)[c.last_direction], (-95,-85)[c.last_direction])[c.burning_center])
	d.skipLine(50, c.largeTopHat.port(), c.LARGE_TOPHAT_LINE, (1, 2)[c.burning_center])
	print "skipped the line!"
	d.forward(50, 1000)
	print "moving forward!"
	w.ao()
	w.msleep(100)
	d.backward(50, 2000)
	print "moving backward!"
