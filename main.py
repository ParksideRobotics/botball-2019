#!/usr/bin/python
import os
import sys

import actions as a
import wallaby as w
import const as c
import drive as d
import util as u

def main():
    if w.create_connect():
        return
    w.create_full()
    w.enable_servos()
    #a.drop_arm()
    a.shake_down()

    print 'waiting for light...'
    u.wait_4_light()
    w.shut_down_in(120)

    w.msleep(2500)
    
    #a.drop_arm()
    a.close_claw()
    #w.msleep(500)

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


    print 'following black line' 
    a.follow_black_line(700)

    w.msleep(500)

    a.close_claw()

    
    
    a.open_claw()

    w.msleep(500)

    a.follow_black_line(700)
    

    print 'closing claw'
    print 'lift arm'
    a.pick_up_arm_and_close_claw()



    print 'dropping pompoms'
    a.move_to_cylinder()

    print 'moving utility zone'
    a.move_to_utility_zone()

    w.msleep(1000)   
    
    w.create_disconnect()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
