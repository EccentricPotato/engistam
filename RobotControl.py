from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from time import sleep
from ev3dev2.sensor.lego import GyroSensor , UltrasonicSensor

class Controls:

    def __init__(self):
        print("Starting...")

    def MoveBackward(self, steering=0, speed=40):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        steer_pair.on(speed, speed)

    def MoveForward(self, steering=0, speed=-40):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        steer_pair.on_for_seconds(steering,speed, seconds=0.01)

    def MoveRight(self):
        gy = GyroSensor()
        gy.mode = 'GYRO-ANG'
        tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
        tank_pair.on(left_speed=30, right_speed=-30)
        gy.wait_until_angle_changed_by(delta=90)
        tank_pair.off()
        sleep(1)

    def MoveLeft(self):
        gy = GyroSensor()
        gy.mode = 'GYRO-ANG'
        tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
        tank_pair.on(left_speed=-30, right_speed=30)
        gy.wait_until_angle_changed_by(delta=90)
        tank_pair.off()
        sleep(1)

    def Measure(self):
        us = UltrasonicSensor()
        return us.distance_centimeters




