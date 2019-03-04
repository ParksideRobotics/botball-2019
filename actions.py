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

def find_burning_center():
	c.camera_servo.enable()
	c.camera_servo.setPosition(1800) # set the servo so It can see both centers, but not cubes
	if not w.camera_open():
		return
	while True:
		w.camera_update()
		best = x.getGreatest(c.BURNING)
		if w.get_object_confidence(c.BURNING, best) < 0.5:
			continue
		x_pos = w.get_object_center_x(c.BURNING, best)
		print x_pos
		if 60 < x_pos < 80:
			print "Close medical center"
			c.burning_center = 0
			break
		elif 90 < x_pos < 120:
			print "Far medical center"
			c.burning_center = 1
			break

def move_to_cubes():
	if not w.camera_open():
		return
	servo_centered = False
	c.camera_servo.setPosition(1024)
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
		if (w.get_camera_width()/2)-10 < w.get_object_center_x(c.YELLOW, best) < (w.get_camera_width()/2)+10:
			servo_centered = True
			break

	print c.camera_servo.position()

	print c.camera_servo.position()/11.3777777778
	print int(c.camera_servo.position()/11.3777777778)
	print int((c.camera_servo.position()/11.3777777778) - 90)
	d.forward(50, 2100)
	d.degreeTurn(10, int((c.camera_servo.position()/11.3777777778) - 110))
	c.camera_servo.setPosition(1024) # reset camera to default position

	exit(0)
		
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