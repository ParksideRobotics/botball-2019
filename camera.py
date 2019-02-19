#!/usr/bin/python
import wallaby as w
import const as c
import drive as d

def getGreatest(channel):
	highestconfidence = 0
	greatest = 0
	for i in range(channel, w.get_object_count(channel)):
			if w.get_object_confidence(channel, i) > highestconfidence:
				highestconfidence = w.get_object_confidence(channel, i)
				greatest = i
	return greatest

def centerX(channel, greatest):
	if w.get_object_center_x(channel, greatest) < (w.get_camera_width() / 2.0) - 20:
		c.leftMotor.off()
		c.rightMotor.motor(50)
	elif w.get_object_center_x(channel, greatest) > (w.get_camera_width() / 2.0) + 20:
		c.rightMotor.off()
		c.leftMotor.motor(50)
