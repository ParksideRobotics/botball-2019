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


    

    print 'waiting for light...'
    w.wait_for_light(c.light.port())
    w.shut_down_in(120)

    
    a.drop_arm()

    a.close_claw()
    w.msleep(500)

    

    print 'moving out of the starting box'
    a.move_out_starbox()  # move out of start box
    

    print 'following gray line'
    a.follow_gray_line(250)

    print 'going back on line'
    a.move_back_on_line()

    print 'following gray line'
    a.follow_gray_line(400)

    print 'turning around'
    a.turn_to_black()       

    print 'open claw'

    a.open_claw()


    print 'following black line' 
    a.follow_black_line(1400)    

    print 'closing claw'
    a.close_claw()

    print 'lift arm'
    a.lift_arm()

    d.forward(100,85)

    d.pivotRight(100, 125)
    
    d.pivotLeft(100,150)

    
    c.claw.setPosition(c.CLAW_OPENED)


   

   
        
    w.msleep(1000)   




    w.create_disconnect()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()

