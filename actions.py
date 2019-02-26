#!/usr/bin/python
import wallaby as w
import const as c
import drive as d
import math
import sys

def skip_line(speed):
        d.driveUntilBlack(100)
        d.driveUntilWhite(100)

def move_out_starbucks():
        """Leave starbucks to get to the main tracking line"""
        skip_line(100)
