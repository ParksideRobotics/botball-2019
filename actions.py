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

def move_out_starbox():
    """Leave starbucks to get to the main tracking line"""
    skip_line(100)
    d.driveUntilGrey(100)
    d.pivotLeft(100,100)


   

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

def turn_to_black():
    d.degreePivot(100, -180)
    
def follow_black_line(dist):
    w.set_create_distance(0)
    while w.get_create_distance() < dist:
        print w.get_create_distance(), w.get_create_rcliff_amt(), w.get_create_lfcliff_amt()
        if w.get_create_rcliff_amt() < c.CREATE_BLACK:
            w.create_drive_direct(100, 0)
        elif w.get_create_rcliff_amt() > c.CREATE_BLACK:
            w.create_drive_direct(0, 100)
    w.create_stop()
            

def open_claw():
    c.claw.setPosition(c.CLAW_OPENED)
    w.msleep(1000)

def drop_arm():
    d.setArmPosition(-10 ,c.ARM_FRONT)
    w.msleep(1000)  

def close_claw():
    c.claw.setPosition(c.CLAW_CLOSED)
    w.msleep(1000)
def  lift_arm():
    d.setArmPosition(10,c.ARM_BACK)
    w.msleep(1000)
    

def shake_down():
    d.setArmPosition(10, c.ARM_BACK )
    w.msleep(500)
    d.setArmPosition(-10,c.ARM_FRONT)   
    w.msleep(500)
    c.claw.setPosition(c.CLAW_OPENED) 
    w.msleep(500) 
    c.claw.setPosition(c.CLAW_CLOSED)
    w.msleep(500) 
    c.claw.setPosition(c.CLAW_OPENED)
    w.msleep(500)
    d.setArmPosition(10,c.ARM_BACK)
    w.msleep(1000)    
    w.create_drive_direct(100,100)    
    w.msleep(500)
    w.create_drive_direct(-100,-100)
    w.msleep(500)   
    w.create_stop()
    

def move_back_on_line():
    d.pivotRight(100,100)
    w.msleep(200)
    d.pivotLeft(100,135)


def move_to_cylinder():
    d.degreePivot(100, -90)
    w.msleep(500)
    d.degreePivot(100, 90)
    w.msleep(500)
    d.setArmPosition(-10 ,c.ARM_FRONT)
    w.msleep(500)
    c.claw.setPosition(c.CLAW_OPENED)



     # ssh root@192.168.125.1
        # cd pynther
        # ./main.py
        # git add .
        # git commit -m "What your code is about, Be specific" 
        # git pull       
    #samadisnumber1 98998989



