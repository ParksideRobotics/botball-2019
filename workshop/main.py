#!/usr/bin/python
import os
import sys
import wallaby as w
import const as x
import drive as d
import actions as a

def main():
	a.exitStart()
	a.setupLineFollow()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()
