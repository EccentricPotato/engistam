#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep

lm1 = LargeMotor("out B")
lm2 = LargeMotor("out A")

'''
This will run the large motor at 50% of its
rated maximum speed of 1050 deg/s.
50% x 1050 = 525 deg/s
'''
lm1.on_for_seconds(speed = 50, seconds=3)
lm2.on_for_seconds(speed = 50, seconds=3)
sleep(1)