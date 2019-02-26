#!/usr/bin/python
import wallaby as w
import const as c
import drive as d
import math
import sys

def skip_line(speed):
        d.driveUntilBlack(100)
        d.driveUntilWhite(100)
        w.create_stop()

def move_out_starbucks():
        """Leave starbucks to get to the main tracking line"""
        skip_line(100)
        d.driveUntilBlack(100)
        d.pivotLeft(100,2500)
        
def follow_gray_line():        
        d.lineFollowUntilTape()

        
