#!/usr/bin/python
import os
import sys

import actions as a
import wallaby as w
import const as c
import utilities as u

def main():
	#u.shake_down()

	#w.wait_for_light(c.light.port())
	w.shut_down_in(120)
	#w.msleep(14000) # wait for other robot
	start_time = w.seconds()

	a.find_burning_center()
	a.move_to_cubes() # use camera to move to cubesS
	a.get_cubes_num(5) # get 5 cubes (all cubes)
	a.move_to_med()

	end_time = w.seconds()
	print "Program took %d seconds" % (end_time - start_time)

if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
