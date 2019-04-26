from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from time import sleep
from ev3dev2.sensor.lego import GyroSensor , UltrasonicSensor
from MeasureDistance import Measuring
from RightLeftMovement import LeftRight

class ForwardMovement:

    def __init__(self):
        print("Starting...")

    def MoveBackward(self, steering=0, speed=40):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        steer_pair.on(speed, speed)

    def MoveForward(self, steering=0, speed=-20):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        steer_pair.on(steering = 0, speed = -20)
        while True:
            dist = Measuring()
            print(dist.Measure())
            if dist.Measure() < 8:
                steer_pair.off()
                print ("I stop")
                turn = LeftRight()
                turn.MoveLeft()
                break










