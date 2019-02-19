#!/usr/bin/python
import wallaby as w
import const as c
import drive as d
import camera as x
import math
import sys

def moveMotor(motor, power, dist): # basically just mtp()
	w.cmpc(motor)
	if dist < 0:
		w.motor(motor, -power)
	else:
		w.motor(motor, power)
	while abs(w.gmpc(motor)) < abs(dist):
		print w.gmpc(motor)
		continue
	print "done!"
	w.motor(motor, 0) # freeze motor, then shut off
	w.off(motor)

def moveDegree(motor, power, degree): # set the motor to a degree, like a servo
	w.cmpc(motor)
	if degree < 0:
		w.motor(motor, -power)
	else:
		w.motor(motor, power)
	goal = degree*5.27
	while abs(w.gmpc(motor)) < abs(goal):
		print w.gmpc(motor)
		continue
	c.distance_traveled += w.gmpc(motor) # set to actual position, not goal
	print "Distance Traveled: %d" % c.distance_traveled,
	print "Goal: %d" % goal
	print "done!"
	w.motor(motor, 0) # freeze motor, then shut off
	w.off(motor)

def resetPosition():
	moveMotor(c.spinner.port(), 50, c.distance_traveled*-1)
	c.distance_traveled = 0 # remember to reset, lol

def move_to_cubes():
	if not w.camera_open():
		return
	while True:
		w.camera_update()
		if w.get_object_count(c.YELLOW) == 0:
			d.spinLeft(50, 1)
			print "spinning left"
		greatest = x.getGreatest(c.YELLOW)
		if w.get_object_confidence(c.YELLOW, greatest) < 0.3:
			continue

		print "X %d, Y %d" % (w.get_object_center_x(c.YELLOW, greatest), w.get_object_center_y(c.YELLOW, greatest))
		# center the object
		x.centerX(c.YELLOW, greatest)

		if w.get_object_bbox_height(c.YELLOW, greatest) > w.get_camera_height() * .9:
			print "Object close!"
			d.stop()
			break

def get_cubes_num(num): # scalable function for getting cubes :))
	degree = 130 # our starting degree for the turn
	for i in range(num):
		if i % 2 == 0:
			moveDegree(c.spinner.port(), 50, degree)
			resetPosition()
			print "FORWARD %d degrees on cube %d" % (degree, i)
		elif i % 2 == 1:
			moveDegree(c.spinner.port(), 50, -degree)
			resetPosition()
			print "BACKWARD %d degrees on cube %d" % (degree, i)
		degree -= 20

def move_to_med(): # move to medical center
	# this code has not been tested yet
	d.degreeTurn(50, 90)
	d.forward(50, 5200)
	