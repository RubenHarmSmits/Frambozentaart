from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''


import time  # import the time library for the sleep function
import brickpi3  # import the BrickPi3 drivers
from Touch_sensor import Touch_sensor_class
from IR_Sensor import IR_Sensor
from Engine import Engine
import math


class Memphis_de_pi:

    def __init__(self):
        self.my_Touch_Sensor = Touch_sensor_class()
        self.my_IR_Sensor = IR_Sensor()
        self.engine_Left = Engine(1)
        self.engine_Right = Engine(2)

    def move_forward(self, speed):
        # print("Moving forward function is starting")
        self.engine_Left.change_speed(speed)
        self.engine_Right.change_speed(speed)
        # print("Moving forward function is finished")

    def move_forward_test(self):
    # print("Moving forward function is starting")
        self.engine_Left.change_speed(31.5)
        self.engine_Right.change_speed(30)
    #     self.engine_Left.change_speed(16)
    #     self.engine_Right.change_speed(15)

    # print("Moving forward function is finished")

    def move_backward(self, speed):
        self.engine_Left.change_speed(-speed)
        self.engine_Right.change_speed(-speed)

    def turn_right(self, speed):
        self.engine_Left.change_speed(speed)
        self.engine_Right.change_speed(-speed)

    def turn_left(self, speed):
        self.engine_Left.change_speed(-speed)
        self.engine_Right.change_speed(speed)

    def stop_move(self):
        self.engine_Left.change_speed(0)
        self.engine_Right.change_speed(0)

    def manage_move(self):
        while True:
            if self.my_Touch_Sensor.get_signal() and self.my_IR_Sensor.isTooClose():
                self.move_backward(30)
                self.turn_left(30)
                print("Turning left")
            elif not self.my_IR_Sensor.isTooClose():
                self.turn_right(20)
                # self.move_forward_test()
                print("Turning right")

            elif not self.my_Touch_Sensor.get_signal() and self.my_IR_Sensor.isTooClose():
                # self.move_forward(40)
                self.move_forward_test()
                print("Moving forward")

            # # Only INFRA
            # if not self.my_IR_Sensor.isTooClose():
            #     self.turn_right(20)
            #     print("Turning right")
            # elif self.my_IR_Sensor.isTooClose():
            #     self.move_forward(20)
            #     print("Moving forward")
            #
            # # Only Touch
            # if self.my_Touch_Sensor.get_signal():
            #     self.turn_left(50)
            # elif not self.my_Touch_Sensor.get_signal():
            #     self.move_forward(50)

            time.sleep(0.02)
            
    def drive_straight(self):

        r_wheel = 31  # mm
        revolutions = get_motor_encoder/ 360   # output motor
        dist_travelled = revolutions*2*math.pi()*r_wheel

        # misschien het dist_diff pas bij >20mm laten triggeren, anders blijft ie corrigeren

        dist1 = 15  # arbitrary value
        dist2 = 5  # arbitrary value
        dist_diff = dist1 - dist2

        alpha = math.degrees(math.atan(dist_diff/dist_travelled))
        correction_angle = 15  # degrees
        gamma = alpha + correction_angle

        correct_distance = 50  # mm
        correct_slanted_distance = (correct_distance / math.degrees(math.cos(correction_angle)))



memphis = Memphis_de_pi()

try:
    # memphis.move_forward(50)
    memphis.manage_move()
    # memphis.move_forward_test()
except KeyboardInterrupt:
    memphis.stop_move()

