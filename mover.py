#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_D
from time import sleep
from ev3dev2.sensor.lego import GyroSensor , UltrasonicSensor
from MeasureDistance import Measuring
from RightLeftMovement import LeftRight
from LightDrill import Drill
from RobotControl import *

control = ForwardMovement()
print("Starting...")
wall = 8

def MovementFunction():
    while True:
        control.MoveForward()
        turn = LeftRight()
        dist = Measuring()
        turn.MoveRight()
        if dist.Measure() > wall:
            break
        else:
            turn.MoveLeft()
            if dist.Measure() > wall:
                break
            else:
                turn.MoveRight()
                if dist.Measure() > wall:
                    break
                else:
                    turn.MoveRight()
                    turn.MoveRight()
                    break
while True:
    MovementFunction()








