import os
import sys

import actions as a
import wallaby as w
import const as c

def main():
	w.wait_for_light(c.light.port())
	w.shut_down_in(120)
	# Our code! godly imo


if __name__ == "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()
	