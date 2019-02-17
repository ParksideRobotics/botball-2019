#!/usr/bin/python
import wallaby as w
import const as c
import math
import sys

distance_traveled = 0 # How far we've traveled
 # Use this so we can return to our start pos

def moveMotor(motor, power, dist):
	w.cmpc(motor)
	w.motor(motor, power)
	while abs(w.gmpc(motor)) < dist:
		print w.gmpc(motor)
		continue
	print "done!"
	w.off(motor)

def moveDegree(motor, power, degree):
	w.cmpc(motor)
	if degree < 0:
		w.motor(motor, -power)
	else:
		w.motor(motor, power)
	goal = degree*5.27
	while w.gmpc(motor) < goal:
		print w.gmpc(motor)
		continue
	distance_traveled += w.gmpc(motor)
	print "done!"
	w.motor(motor, 0) # freezing motor instead of turning off, more accurate

def resetPosition():
	moveMotor(c.spinner.port(), 50, distance_traveled)

def get_cubes():
	print "moving to get first cube"
	# moveMotor(c.spinner.port(), -50, int(sys.argv[1])) # tick is 700 using argv for testing
	moveDegree(c.spinner.port(), 50, int(sys.argv[1]))
	print "moving to get second cube"
	# moveMotor(c.spinner.port(), 50, int(sys.argv[2])) # tick is 1300
	moveDegree(c.spinner.port(), 50, int(sys.argv[2]))
	resetPosition()