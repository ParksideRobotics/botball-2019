#!/usr/bin/python
import wallaby as w
import drive as d
import const as c

def exitStart():
	d.forward(100, 1000)
	d.spinLeft(100, 600)
	d.forward(100, 4000)

def setupLineFollow():
	d.driveUntilBlack(100)
	while w.analog(c.largeTopHat) > c.LARGE_TOPHAT_LINE:
		d.forward(100, 1)
	while w.analog(c.largeTopHat) < c.LARGE_TOPHAT_LINE:
		d.spinLeft(100, 1)
	d.lineFollowUntilTape()
