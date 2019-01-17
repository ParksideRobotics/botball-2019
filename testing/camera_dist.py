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

		distance = pow(((2.3*15*get_camera_height()) / (get_object_bbox_height(green, greatest)*40)), 2) - 10
		# Focal Length * Real Object Height * Camera Height / object height (pixels) * sensor height 
		# Squaring, then minus 10. At small numbers, doesn't matter. But at large numbers will be more accurate (testing)

		print "Distance: %fmm" % distance

	camera_close()

if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
	sys.stdout.flush()
