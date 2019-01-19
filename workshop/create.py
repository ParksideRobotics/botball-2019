#!/usr/bin/python
import os
import sys
from wallaby import *

ET = Analog(0)
Tophat = Analog(1)
Light = Analog(2)

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
		create_drive_direct(100, 0)
	elif get_object_center_x(channel, greatest) > (get_camera_width() / 2.0) + 20:
		create_drive_direct(0, 100)

def main():
	create_connect()
	gyro_calibrate()
	while True:
		print "X %d, Y %d, Z %d" % (gyro_x(), gyro_y(), gyro_z())
		create_stop()
	
if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
	main()