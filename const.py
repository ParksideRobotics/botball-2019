#!/usr/bin/python
import wallaby as w

# motors

# servo

# sensors
largeTopHat = 0
rangeFinder = 1
smallTopHat = 2
pushButton = 0


pushButton = w.Digital(0)
largeTopHat = w.Analog(0)
rangeFinder = w.Analog(1)
smallTopHat = w.Analog(2)
light = w.Analog(3) # Not actually on robot yet

# Line
CREATE_LINE = 2500
LARGE_TOPHAT_LINE = 1800
SMALL_TOPHAT_LINE = 2800
