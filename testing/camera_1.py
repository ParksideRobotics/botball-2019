#!/usr/bin/python
import os
import sys
import math
from wallaby import *

previous = 0

def centerX(channel, greatest):
	if get_object_center_x(channel, greatest) < (get_camera_width() / 2.0) - 10:
		set_servo_position(0, get_servo_position(0)+50)
	elif get_object_center_x(channel, greatest) > (get_camera_width() / 2.0) + 10:
		set_servo_position(0, get_servo_position(0)-50)

def centerX_with_complicated_math(best):
	global previous
	x = get_object_center_x(0, best)
	y = get_object_center_y(0, best)

	tolerance = 5
	if previous - tolerance < x < previous + tolerance: # if the new x is only a 10 pixel difference, we don't care
		return
	previous = x

	print "Cube:",
	print x,
	print y,
	print get_object_confidence(0, best)

	angle = math.atan2(y, x) * 100
	print angle
	new_pos = int(11.37777777777778*angle)
	print "Actual servo tick: %d " % new_pos
	set_servo_position(0, new_pos) # magic number that should move us to it? idk man
	print get_servo_position(0)
	#while abs(get_servo_position(0)) + 1 < abs(new_pos): # to make sure that we don't loop until after we already moved to our position
	#	pass

def main():
	s = Servo(0)
	if not camera_open():
		return
	s.setPosition(1024) # starting pos
	s.enable()
	while True:
		camera_update()
		objects = get_object_count(0)
		if objects == 0:
			print "no objects!"
			continue
		best = max((get_object_confidence(0,i),i) for i in range(objects))[1] # thanks for letting me 'borrow' code
		if get_object_confidence(0, best) < 0.5:
			continue
	
		print "Cube:",
		print get_object_center_x(0, best),
		print get_object_confidence(0, best)

		centerX(0, best)

if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
