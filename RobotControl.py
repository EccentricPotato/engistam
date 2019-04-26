from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_D
from time import sleep
from ev3dev2.sensor.lego import GyroSensor , UltrasonicSensor
from MeasureDistance import Measuring
from RightLeftMovement import LeftRight
from LightDrill import Drill

class ForwardMovement:

    def __init__(self):
        print("")

    def MoveBackward(self, steering=0, speed=40):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        steer_pair.on_for_seconds(steering = 0,speed = 20, seconds=2, brake=True, block=True)

    def MoveForward(self, steering=0, speed=-20):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        steer_pair.on_for_seconds(steering = 0,SpeedRPM = 24, seconds=5, brake=True, block=True)
        while True:
            dist = Measuring()
            drill = Drill()
            if dist.Measure() < 8:
                steer_pair.off()
                sleep(1)
                print ("I stop")
                turn = LeftRight()
                turn.MoveLeft()
                break
            if drill.Drilling() == 1:
                steer_pair.off()
                print("drilling")
                sleep(2)
                mm = MediumMotor(OUTPUT_D)
                mm.on_for_seconds(speed=40, seconds=10)
                break











