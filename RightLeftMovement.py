from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from time import sleep
from ev3dev2.sensor.lego import GyroSensor , UltrasonicSensor
from MeasureDistance import Measuring

class LeftRight:
    def __init__(self):
        print("Turning...")

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
        tank_pair.on_for_degrees(left_speed = 10, right_speed = -10, degrees =270, brake=True, block=True)

        tank_pair.off()
        sleep(2)