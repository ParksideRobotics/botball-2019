#!/usr/bin/python
import wallaby as w
import const as c
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

def get_cubes(): # get 2 cubes
	print "moving to get first cube"
	moveDegree(c.spinner.port(), 50, int(sys.argv[1]))
	resetPosition()
	print "moving to get second cube"
	moveDegree(c.spinner.port(), 50, int(sys.argv[2]))
	resetPosition()

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
