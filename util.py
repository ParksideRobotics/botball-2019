#!/usr/bin/python
import wallaby as w
import const as c

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
    if lightOn > 3000:
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
    if lightOff < 3000:
        print("Bad calibration")
        return False


    if (lightOff - lightOn) < 1000:
        print("Bad calibration")
        return False
    startLightThresh = (lightOff + lightOn) / 2
    print("Good calibration! ", startLightThresh)
    print('{} {} {}'.format(lightOff, lightOn, startLightThresh))
    return startLightThresh
