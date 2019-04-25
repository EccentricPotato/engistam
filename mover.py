#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, OUTPUT_A, OUTPUT_B
from time import sleep

steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)

steer_pair.on_for_seconds(steering=0, speed=50, seconds=2)

sleep(1)