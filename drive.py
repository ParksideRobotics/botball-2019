#!/usr/bin/python
import wallaby as w
import const as c

def stop():
    w.create_stop()

def clear_ticks():
    w.set_create_distance(0)

def driveMotor(left, right, ticks):
    clear_ticks()
    w.create_drive_direct(left, right)
    while abs(w.get_create_distance()) < abs(ticks):
        print w.get_create_distance()
        continue
    w.create_stop()

def forward(speed, ticks):
    clear_ticks()
    w.create_drive_straight(speed)
    while w.get_create_distance() < ticks:
        continue
    w.create_stop()

def backward(speed, ticks):
    clear_ticks()
    w.create_drive_straight(speed*-1)
    while abs(w.get_create_distance()) < ticks:
        continue
    w.create_stop()

def spinLeft(speed, ticks):
    driveMotor(speed*-1, speed, ticks)

def spinRight(speed, ticks):
    driveMotor(speed, speed*-1, ticks)

def veerLeft(speed, ticks, o):
    driveMotor((speed*-1)-o, speed, ticks)

def veerRight(speed, ticks, o):
    driveMotor(speed, (speed*-1)-o, ticks)

def pivotLeft(speed, ticks):
    driveMotor(0, speed, ticks)

def pivotRight(speed, ticks):
    driveMotor(speed, 0, ticks)

def radiusTurn(speed, radius, ticks):
    driveMotor(speed, int((radius / (radius+5.0)*speed), ticks))

def driveUntilBlack(speed):
    while w.get_create_lfcliff_amt() > c.CREATE_BLACK:
        w.create_drive_straight(speed)

def driveUntilWhite(speed):
    while w.get_create_lfcliff_amt() < c.CREATE_GREY:
        w.create_drive_straight(speed)

def driveUntilGrey(speed):
    while w.get_create_lfcliff_amt() > c.CREATE_GREY:
        w.create_drive_straight(speed)


    

def lineFollowUntilTape(line):
    while w.get_create_lfcliff_amt() < line:
        if w.get_create_rfcliff_amt() < line:
            veerLeft(50, 1, 10)
        elif w.get_create_rcliff_amt() > line:
            veerRight(50, 1, 10)

def degreeTurn(speed, degree):
    w.set_create_total_angle(0)
    if degree < 0:
        w.create_spin_CW(speed)
    else:
        w.create_spin_CCW(speed)
    while abs( w.get_create_total_angle() ) < abs( degree*1.15 ):
        continue
    w.create_stop()

def degreePivot(speed, degree): 
    w.set_create_total_angle(0)
    if degree < 0:
        w.create_drive_direct(100, -90)
    else:
        w.create_drive_direct(-90, 100)
    while abs( w.get_create_total_angle() ) < abs( degree*1.15 ):
        continue
    w.create_stop()


