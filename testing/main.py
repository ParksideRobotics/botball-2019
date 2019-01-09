#!/usr/bin/python
import os, sys
from wallaby import *

#MOTORS
leftMotor = 0
rightMotor = 1

def main():
	if not camera_open():
		print "camera could not be opened"
		return

	while True:	
		camera_update()
		greatest = 0					   # Greatest Object
		highestconfidence = 0			   # Highest confidence
		object_count = get_object_count(0) # Object count
		green = 0						   # Channel

		if object_count == 0:
			continue

		#print 'there are %d objects' % object_count
			
		for i in range(green, object_count):
			#print 'object %d confidence: %.4f' % (i, get_object_confidence(green, i))
			if get_object_confidence(green, i) > highestconfidence:
				highestconfidence = get_object_confidence(green, i)
				greatest = i

		print 'object %d is greatest' % greatest
		print 'object x: %d y: %d' % (get_object_center_x(green, greatest), get_object_center_y(green, greatest))

		if get_object_center_x(green, greatest) < (get_camera_width() / 2.0) - 20:
			motor(leftMotor, 25)
			off(rightMotor)
		elif get_object_center_x(green, greatest) > (get_camera_width() / 2.0) + 20:
			motor(rightMotor, -25)
			off(leftMotor)
		else:
			ao()

	camera_close()

if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
	sys.stdout.flush()