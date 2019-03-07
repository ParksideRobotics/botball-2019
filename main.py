#!/usr/bin/python
import os
import sys

import actions as a
import wallaby as w
import const as c

def main():
	# w.wait_for_light(c.light.port())
	# w.shut_down_in(120)

	a.find_burning_center()
	a.move_to_cubes() # use camera to move to cubes
	a.get_cubes_num(5) # get 5 cubes (all cubes)
	a.move_to_med()


if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
