#!/usr/bin/python
import wallaby as w
import const as c
import drive as d
import math
import sys


def skip_line(speed):
    d.driveUntilBlack(speed)
    d.driveUntilWhite(speed)
    w.create_stop()


def move_out_starbucks():
    """Leave starbucks to get to the main tracking line"""
    skip_line(100)
    d.driveUntilBlack(100)
    d.pivotLeft(100,250)
    #d.spinLeft(100, 2500)

def follow_gray_line(dist):
    w.set_create_distance(0)
    while w.get_create_distance() < dist:
        # print w.get_create_lcliff_amt()
        print w.get_create_distance()
        if w.get_create_rfcliff_amt() < c.CREATE_GREY:
            w.create_drive_direct(100, 10)
        elif w.get_create_lfcliff_amt() < c.CREATE_GREY:
            w.create_drive_direct(10, 100)
            print "Done! on the line"
    while w.get_create_rfcliff_amt() > c.CREATE_BLACK:
        w.create_drive_direct(0, 100)
    w.create_stop()

def move_to_black():
    d.spinRight(100,375)
    w.create_spin_block()
    exit(0)

def follow_black_line(dist):
    w.set_create_distance(0)
    while w.get_create_distance() < dist:
        print w.get_create_distance(), w.get_create_rcliff_amt(), w.get_create_lfcliff_amt()
        if w.get_create_rcliff_amt() < c.CREATE_BLACK:
            w.create_drive_direct(0, 100)
        elif w.get_create_rcliff_amt() > c.CREATE_BLACK:
            w.create_drive_direct(100, 50)
            
        # print "samadisnumber1"
        

        # ssh root@192.168.125.1
        # cd pynther
        # ./main.py
        
