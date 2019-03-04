#!/usr/bin/python
import os
import sys

import actions as a
import wallaby as w
import const as c

def main():
        if w.create_connect():
                return
        w.create_full()
	# w.wait_for_light(c.light.port())
	# w.shut_down_in(120)

	a.move_out_starbucks() # move out of start box
	# ARGV PARAMETERS ARE NOT FINAL CODE!
	a.follow_gray_line(int(sys.argv[1])) # putting this in so we can play with values 
        a.follow_black_line(int(sys.argv[2])) # putting this in so we can play with values

	
	w.create_disconnect()


if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main()
