#!/usr/bin/python
#this file was edited!
import os
import sys
from wallaby import *

def main():
	# camera_load_config("eeee")
	if not camera_open():
		print "camera could not be opened"
		return
	camera_update()
	highestconfidence = 0
	while True:		
		greatest = 0
		print 'there are %d objects' % get_object_count(0)
		if get_object_count(0) == 0:
			camera_update()
			continue
			
		for i in range(0, get_object_count(0)):
			print 'object %d confidence: %.4f' % (i, get_object_confidence(0, i))
			if get_object_confidence(0, i) > highestconfidence:
				highestconfidence = get_object_confidence(0, i)
				greatest = i

		# print 'object %d is greatest' % greatest
		# print 'object x: %d y: %d' % (get_object_center_x(0, greatest), get_object_center_x(0, greatest))
                
		camera_update()

    #if not camera_update():
	#	print "camera couldn't update"
	#	return
	
	camera_close()

if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
	sys.stdout.flush()
