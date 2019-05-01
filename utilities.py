#!/usr/bin/python
import wallaby as w
import drive as d
import const as c
import camera as x
import sys

def _init():
	c.collection_arm.enable()
	c.camera_servo.enable()

def shake_down():
	c.collection_arm.enable()
	c.collection_arm.setPosition(1550)
	w.msleep(1500)
	d.forward(50, 1000)
	print "moving forward"
	w.msleep(500)
	print "moving backward"
	d.backward(50, 1000)
	w.msleep(500)
	moveDegree(c.spinner.port(), 50, 90)
	print "spinning +90 degrees"
	w.msleep(500)
	moveDegree(c.spinner.port(), 50, -90)
	print "spinning -90 degrees"
	w.msleep(500)
	c.camera_servo.enable()
	c.camera_servo.setPosition(2047)
	print "-90 servo"
	w.msleep(500)
	c.camera_servo.setPosition(900)
	print "+90 servo"
	w.msleep(500)
	c.camera_servo.setPosition(0)
	print "+90 servo"
	w.msleep(500)
	d.driveUntilBlack(50)
	print "checking tophat!"
	w.msleep(500)
	print "testing the camera and burning centers!"
	w.console_clear()
	print "Not Ready! Awaiting input!"
	while not w.left_button():
		pass

def moveMotor(motor, power, dist): # basically just mtp()
	w.cmpc(motor)
	if dist < 0:
		w.motor(motor, -power)
	else:
		w.motor(motor, power)
	while abs(w.gmpc(motor)) < abs(dist):
		print w.gmpc(motor)
		continue
	w.motor(motor, 0) # freeze motor, then shut off
	w.off(motor)

def moveDegree(motor, power, degree): # set the motor to a degree, like a servo
	w.cmpc(motor)
	if degree < 0:
		w.motor(motor, -power)
	else:
		w.motor(motor, power)
	goal = c.MOTOR_DEG2TICK(degree)
	while abs(w.gmpc(motor)) < abs(goal):
		print w.gmpc(motor)
		continue
	c.distance_traveled += w.gmpc(motor) # set to actual position, not goal
	print "Distance Traveled: %d" % c.distance_traveled,
	print "Goal: %d" % goal
	print "done!"
	w.motor(motor, 0) # freeze motor, then shut off
	w.off(motor)

def isOnLine(sensor, line):
	return True if w.analog(sensor) > line else False

def resetPosition():
	moveMotor(c.spinner.port(), 50, c.distance_traveled*-1)
	c.distance_traveled = 0 # remember to reset, lol

def wait_4_light():
	thresh = 0
	while not thresh: 
		thresh = calibrate(c.light.port())
	while c.light.value() > thresh:
		pass

def calibrate(port):
    print("Press LEFT button with light on")
    while not w.left_button():
        pass
    while w.left_button():
        pass
    lightOn = w.analog(port)
    print("On value =", lightOn)
    if lightOn > 4000:
        print("Bad calibration")
        return False
    w.msleep(1000)
    print("Press RIGHT button with light off")
    while not w.right_button():
        pass
    while w.right_button():
        pass
    lightOff = w.analog(port)
    print("Off value =", lightOff)
    if lightOff < 1000:
        print("Bad calibration")
        return False


    if (lightOff - lightOn) < 1:
        print("Bad calibration")
        return False
    startLightThresh = (lightOff + lightOn) / 2
    print("Good calibration! ", startLightThresh)
    print('{} {} {}'.format(lightOff, lightOn, startLightThresh))
    return startLightThresh

def burning_center_test():
	c.camera_servo.enable()
	c.camera_servo.setPosition(1400) # set the servo so It can see both centers, but not cubes
	c.collection_arm.setPosition(270) # set the arm to so it is open
	d.forward(50, 650)
	d.spinLeft(50, 100)
	if not w.camera_open():
		return
	while not w.right_button():
		w.camera_update()
		best = x.getGreatest(c.BURNING)
		if w.get_object_confidence(c.BURNING, best) < 0.2:
			continue
		x_pos = w.get_object_center_x(c.BURNING, best)
		print x_pos
		if 0 < x_pos < 79:
			print "Close medical center"
			break
		elif 80 < x_pos < 140:
			print "Far medical center"
			break
