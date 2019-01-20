#!/usr/bin/python
import os
import sys
from wallaby import *
import const as x

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
		if get_object_count(x.RED) == 0:
			create_drive_direct(-100, 100) #spin left
		greatest = getGreatest(x.RED)
		if get_object_confidence(x.RED, greatest) < 0.3:
			continue

		print "X %d, Y %d" % (get_object_center_x(x.RED, greatest), get_object_center_y(x.RED, greatest))
		# center the object
		centerX(x.RED, greatest)

		if get_object_bbox_height(x.RED, greatest) > get_camera_height() * .9:
			print "Object close!"
			create_stop()
			break

if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
	main()
