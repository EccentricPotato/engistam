#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, OUTPUT_A, OUTPUT_B
from time import sleep


def MoveBackward(steering = 0, speed = 40):
    steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
    steer_pair.on_for_seconds(steering, speed, seconds=1)

def MoveForward(steering = 0, speed = -40):
    steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
    steer_pair.on_for_seconds(steering, speed, seconds=1)

def MoveRight()
    tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
    tank_pair.on_for_degrees(left_speed = 20, right_speed = 0, degrees = 90, brake=True, block=True)


def MoveLeft()
    tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
    tank_pair.on_for_degrees(left_speed=0, right_speed=20, degrees=90, brake=True, block=True)


MoveForward()
MoveRight()
MoveLeft()
sleep(1)