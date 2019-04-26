from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from time import sleep
from ev3dev2.sensor.lego import GyroSensor , UltrasonicSensor

class Measuring:
    def __init__(self):
        print("")

    def Measure(self):
        us = UltrasonicSensor()
        return us.distance_centimeters