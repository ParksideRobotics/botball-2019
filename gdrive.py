import wallaby as w
import const as c
import math

# this code was pretty much stolen
# but will test, why not

def _clear_():
	w.cpmc(c.leftMotor.port())
	w.cpmc(c.rightMotor.port())

def freeze():
	c.leftMotor.motor(0)
	c.rightMotor.motor(0)

def calibrate():
	i = 0
	avg = 0
	while i < 50:
		avg += w.Gyro.z()
		w.msleep(1)
		i += 1
	c.bias = avg / i
	w.msleep(60)

def turn_with_gyro(left_wheel_speed, right_wheel_speed, target_theta_deg):
    calibrate()
    print("turning")
    target_theta = round(target_theta_deg * c.turn_conversion)
    theta = 0
    while theta < target_theta:
        c.leftMotor.motor(left_wheel_speed)
		c.rightMotor.motor(right_wheel_speed)
        msleep(10)
        theta = theta + abs(w.gyro_z() - c.bias) * 10
    print(theta)
    freeze()


def drive_with_gyro(speed, time):
	theta = 0
	start_time = w.seconds()
	while w.seconds - start_time < (time / 1000.0):
		if speed > 0:
			c.leftMotor.moveAtVelocity(int(speed - speed * (1.920137e-16 + 0.000004470956*theta)))
			c.rightMotor.moveAtVelocity(int(speed + speed *(1.920137e-16 + 0.000004470956*theta)))
		else:
			c.leftMotor.moveAtVelocity(int(speed + speed * (1.920137e-16 + 0.000004470956*theta)))
			c.rightMotor.moveAtVelocity(int(speed - speed * (1.920137e-16 + 0.000004470956*theta)))
		w.msleep(10)
		theta += (w.gyro_z() - bias) * 10
