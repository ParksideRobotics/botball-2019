#!/usr/bin/python
import os
import sys
from wallaby import *

def main():
	s = Servo(0)
	if not camera_open():
		return
	w = get_camera_width()
	h = get_camera_height()
	s.enable()
	while True:
		camera_update()
		objects = get_object_count(0)
		if objects == 0:
			print "no objects!"
			continue
		best = max((get_object_confidence(0,i),i) for i in range(objects))[1] # thanks for letting me 'borrow' code
		x = get_object_center_x(0, best)
		y = get_object_center_y(0, best)
		print x,
		print y
		if x < w/2 - 20:
			s.setPosition(2047)
		elif x > w/2 + 20:
			s.setPosition(0)

if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()