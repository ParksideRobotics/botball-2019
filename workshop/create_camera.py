#!/usr/bin/python
import os
import sys
from wallaby import *

ET = Analog(0)
Tophat = Analog(1)
Light = Analog(2)

# Channel Names
yellow = 0
green  = 1
red    = 2

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
		create_drive_direct(0, 100)
	elif get_object_center_x(channel, greatest) > (get_camera_width() / 2.0) + 20:
		create_drive_direct(100, 0)

def main():
	create_connect()
	if not camera_open():
		return
	while True:
		camera_update()
		if get_object_count(red) == 0:
			create_drive_direct(-100, 100) #spin left
		greatest = getGreatest(red)
		if get_object_confidence(red, greatest) < 0.3:
			continue

		print "X %d, Y %d" % (get_object_center_x(red, greatest), get_object_center_y(red, greatest))
		# center the object
		centerX(red, greatest)

		if get_object_bbox_height(red, greatest) > get_camera_height() * .95:
			print "Object close!"
			create_stop()

if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
	main()
