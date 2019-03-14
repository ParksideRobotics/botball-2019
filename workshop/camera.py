#!/usr/bin/python
import wallaby as w


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
