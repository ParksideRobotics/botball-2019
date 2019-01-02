#!/usr/bin/python
import os, sys
from wallaby import *

def main():
	# camera_load_config("eeee")
	if not camera_open():
		print "camera could not be opened"
		return
	while True:
		highestconfidence = 0
		greatest = 0
		print 'there are %d objects' % get_object_count(0)
		if get_object_count(0) == 0:
			continue
		for i in range(0, get_object_count(0)):	
			if get_object_confidence(0, i) > highestconfidence:
				highestconfidence = get_object_confidence(0, i)
				greatest = i
		print 'object %d is greatest' % greatest
		if get_object_center(0, greatest).x > get_camera_width()/2:
			fd(0)
			bd(1)
        if get_object_center(0, greatest).x < get_camera_width()/2:
			fd(1)
			bd(0)    
                
	if not camera_update():
		print "camera couldn't update"
		return

if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
	print 'asdfas'
	sys.stdout.flush()
