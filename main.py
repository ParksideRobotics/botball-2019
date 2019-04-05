#!/usr/bin/python
import os
import sys

import actions as a
import wallaby as w
import const as c
import utilities as u

def main():
	u._init()
	u.shake_down()
	u.wait_4_light()
	w.shut_down_in(120)
	start_time = w.seconds()

	a.move_out_startbox()
	a.find_burning_center()
	a.move_to_cubes() # use camera to move to cubes
	a.get_cubes_num(5) # get 5 cubes (all cubes)
	a.move_to_med()
	a.return_to_med()

	end_time = w.seconds()
	print "%s medical center" % ("Close", "Far")[c.burning_center]
	print "%s the cubes" % ("NOT," "YES")[c.can_see]
	print "Program took %f seconds" % (end_time - start_time)
	
if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
