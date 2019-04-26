#!/usr/bin/env python3
from RobotControl import *

control = Controls()
while True:
    control.Measure()
    if control.Measure() < 8:
         print ("I stop")
         control.MoveLeft()
    else:
        control.MoveForward()


