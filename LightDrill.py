from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_D
from time import sleep
from ev3dev2.sensor.lego import GyroSensor , UltrasonicSensor, ColorSensor
from MeasureDistance import Measuring

class Drill:

    def __init__(self):
        print("")


    def Drilling(self):
        cl = ColorSensor()
        cl.mode = 'COL-COLOR'
        print(cl.color)
        return cl.color




