#!/usr/bin/python
import os
import sys
from wallaby import *

def main():
    print "Hello World"
    if camera_open() != 1:
        print 'couldnt open camera'
        return
    camera_width = float(get_camera_width())
    while True:
        camera_update()
        obj_count = get_object_count(0)
        if obj_count == 0:
            print 'no objects'
            continue
        best_object = max((get_object_confidence(0,i),i) for i in range(obj_count))[1]
        x_position = get_object_center_x(0,best_object)
        fraction = x_position / camera_width
        print '-' * int(fraction*100) + '[ ]' + '-' * int((1-fraction)*100)

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()
