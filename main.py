#!/usr/bin/python
import os
import sys

import actions as a
import wallaby as w
import const as c
import drive as d



def main():
    if w.create_connect():
        return
    w.create_full()
    w.enable_servos()
    a.shake_down()
    

    # print 'waiting for light...'
    # w.wait_for_light(c.light.port())
    # w.shut_down_in(120)

    
    c.arm.setPosition(200)
    c.claw.setPosition(0)

    print 'moving out of the starting box'
    a.move_out_starbox()  # move out of start box

    print 'following gray line'
    a.follow_gray_line(630)

    print 'turning around'
    a.turn_to_black()

    print 'moving claw'
    a.move_claw() # put this in for testing

    print 'following black line'
    a.follow_black_line(900)
     
    print 'moving claw'
    a.move_claw() # put this in for testing

    w.create_disconnect()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

