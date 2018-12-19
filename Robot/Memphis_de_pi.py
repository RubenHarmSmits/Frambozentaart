from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

import time  # import the time library for the sleep function
import brickpi3  # import the BrickPi3 drivers
import Touch_Sensor
import IR_Sensor
import Engine


# Configure for an EV3 color sensor.
# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# BP.Sensor_TYPE.EV3_INFRARED_PROXIMITY specifies that the sensor will be an EV3 infrared sensor.
my_Touch_Sensor = Touch_Sensor()
my_IR_Sensor = IR_Sensor()
engine_Left = Engine()
engine_Right = Engine()

class Memphis_de_pi:

    def __init__(self):
        self.This_Touch_Sensor

    def move_forward(speed):
        engine_Left.change_speed(speed)
        engine_Right.change_speed(speed)

    def turn_right():
        engine_Left.change_speed(50)
        engine_Right.change_speed(-50)

    def turn_left():
        engine_Left.change_speed(-50)
        engine_Right.change_speed(50)

    def manage_move():
        while True:
            if my_Touch_Sensor.get_signal() and my_IR_Sensor.isTooClose():
                turn_left()
            elif not my_IR_Sensor.isTooClose():
                turn_right()
            elif not my_Touch_Sensor.get_signal() and not my_IR_Sensor.isTooClose():
                move_forward(50)
                time.sleep(0.02)

# def turn_left(speed):
#     print("turning left")
#     BP.set_motor_power(BP.PORT_A, -speed)
#     BP.set_motor_power(BP.PORT_D, speed)
#
# def turn_right(speed):
#     print("turning left")
#     BP.set_motor_power(BP.PORT_A, speed)
#     BP.set_motor_power(BP.PORT_D, -speed)
#
# def move_forward(speed):
#     print("moving forward")
#     BP.set_motor_power(BP.PORT_A, speed)
#     BP.set_motor_power(BP.PORT_D, speed)
#
# def move_back():
#     print("moving back")
#     BP.set_motor_power(BP.PORT_A, -50)
#     BP.set_motor_power(BP.PORT_D, -50)
#
#
# try:
#     while True:
#         infrared_proximity = BP.get_sensor(BP.PORT_3)
#         print(infrared_proximity, type(infrared_proximity))
#
#         if infrared_proximity < 50:  # if the touch sensor is pressed
#             speed = 50
#             move_forward(speed)
#             print("Moving forward ")
#
#         elif infrared_proximity > 49:  # else the touch sensor is not pressed or not configured, so set the speed to 0
#             speed = 30
#             turn_right(speed)
#             print("Turning_right")
#
#         time.sleep(0.02)
#
# except KeyboardInterrupt:
#     BP.reset_all()