#!/usr/bin/python
import os
import sys
from wallaby import *

ET = Analog(0)
Tophat = Analog(1)
Light = Analog(2)

def main():
	create_connect()
	t = 2500
	while True:
		print "LF %d, RF %d" % (get_create_lfcliff_amt(), get_create_rfcliff_amt())
		if get_create_lfcliff_amt() > t or get_create_rfcliff_amt() > t:
			print "Not on line!"	
		elif get_create_lfcliff_amt() < t or get_create_rfcliff_amt() < t:
			print "ON LINE!!!"
			print "ONLINE VALUE: L %d R %d" % (get_create_lfcliff_amt(), get_create_rfcliff_amt())

		if get_create_lfcliff_amt() > t:
			create_drive_direct(100, 0)
		elif get_create_rfcliff_amt() > t:
			create_drive_direct(0, 100)
		#elif get_create_lfcliff_amt() > t and get_create_rfcliff_mat() > t:
		#	create_drive_direct(100, 100)

if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
	main()
