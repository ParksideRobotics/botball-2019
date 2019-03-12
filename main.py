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
    # print 'waiting for light...'
    # w.wait_for_light(c.light.port())
    # w.shut_down_in(120)

    print 'moving out of the starting box'
    a.move_out_starbucks()  # move out of start box

    # ARGV PARAMETERS ARE NOT FINAL CODE!
    # putting this in so we can play with values
    print 'following gray line'
    a.follow_gray_line(int(sys.argv[1]))

    print 'turning around'
    a.move_to_black()

    # putting this in so we can play with values
    print 'following black line'
    a.follow_black_line(int(sys.argv[2]))

    w.create_disconnect(    )

    
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
