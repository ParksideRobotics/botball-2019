#!/usr/bin/python
import os
import sys
from wallaby import *

#MOTORS
leftMotor = 0
rightMotor = 1

def getGreatest(channel):
	highestconfidence = 0
	greatest = 0
	for i in range(channel, get_object_count(channel)):
			if get_object_confidence(channel, i) > highestconfidence:
				highestconfidence = get_object_confidence(channel, i)
				greatest = i
	return greatest

def centerX(channel, greatest):
	if get_object_center_x(channel, greatest) < (get_camera_width() / 2.0) - 20:
		motor(leftMotor, 25)
		off(rightMotor)
	elif get_object_center_x(channel, greatest) > (get_camera_width() / 2.0) + 20:
		motor(rightMotor, -25)
		off(leftMotor)

def main():
	if not camera_open():
		print "camera could not be opened"
		return

	while True:	
		camera_update() # Channel
		object_count = get_object_count(0)
		green = 0
		greatest = getGreatest(green)

		if object_count == 0:
			continue
		if get_object_confidence(green, greatest) < .3:
			continue

		print 'object %d is greatest' % greatest
		print 'object x: %d y: %d' % (get_object_center_x(green, greatest), get_object_center_y(green, greatest))

		centerX(green, greatest)

		if get_object_bbox_height(green, greatest) < get_camera_height() * .8:
			motor(leftMotor, 25)
			motor(rightMotor, -25)

		ao()

	camera_close()

if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
	sys.stdout.flush()
