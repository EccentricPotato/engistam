#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from time import sleep
from ev3dev2.sensor.lego import GyroSensor


def MoveBackward(steering = 0, speed = 40):
    steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
    steer_pair.on_for_seconds(steering, speed, seconds=1)

def MoveForward(steering = 0, speed = -40):
    steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
    steer_pair.on_for_seconds(steering, speed, seconds=1)

def MoveRight():
    gy = GyroSensor()
    gy.mode = 'GYRO-ANG'
    tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
    tank_pair.on(left_speed=100, right_speed=-100)

    while gy.value() != 90:  # while gyro sensor is not turned to 90 deg
        print(gy.value())
        sleep(0.01)
    tank_pair.off()
    sleep(5)


def MoveLeft():
    tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
    tank_pair.on_for_degrees(left_speed=-100, right_speed=100, degrees=300, brake=True, block=True)


MoveForward()
MoveRight()
MoveLeft()
"""sleep(1)
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
tank_pair.off()
sleep(5)"""