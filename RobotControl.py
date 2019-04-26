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
    is_drilled = False

    def __init__(self):
        print("")

    def MoveBackward(self, steering=0, speed=40):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        steer_pair.on_for_seconds(steering = 0,speed = 20, seconds=2, brake=True, block=True)

    def MoveForward(self, steering=0, speed=-20):
        steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
        drill = Drill()
        #We make this condition to check if the Robot
        if drill.Drilling() == 1:
            steer_pair.off()
            if self.is_drilled == False:
                self.is_drilled = True
                print("drilling")
                sleep(2)
                mm = MediumMotor(OUTPUT_D)
                sp = SpeedRPM(90)
                time = 10
                mm.on_for_seconds(speed=sp, seconds=time)

                print("Number of rotations ="+str(sp/time))

        else:
            steer_pair.on_for_seconds(steering=0, speed=-1 * SpeedRPM(12), seconds=1, brake=True, block=True)
