
from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

import time  # import the time library for the sleep function
import brickpi3  # import the BrickPi3 drivers


BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.


def turn_left(speed):
    print("turning left")
    BP.set_motor_power(BP.PORT_A, -speed)
    BP.set_motor_power(BP.PORT_D, speed)


def move_forward(speed):
    print("moving forward")
    BP.set_motor_power(BP.PORT_A, speed)
    BP.set_motor_power(BP.PORT_D, speed)

def move_back():
    print("moving back")
    BP.set_motor_power(BP.PORT_A, -50)
    BP.set_motor_power(BP.PORT_D, -50)




BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)  # Configure for a touch sensor. If an EV3 touch sensor is connected, it will be configured for EV3 touch, otherwise it'll configured for NXT touch.

try:
    print("Press touch sensor on port 1 to run motors")
    value = 0
    while not value:
        try:
            print("First loop: before get_sensor ")
            value = BP.get_sensor(BP.PORT_1)
            time.sleep(0.5)
            print("First loop: after get_sensor ")
        except brickpi3.SensorError:
            pass

    speed = 30
    while True:
        value = BP.get_sensor(BP.PORT_1)
        print("Second loop: before get_sensor ")
        if value:  # if the touch sensor is pressed
            print("Third: before get_sensor ")
            speed = 50
            move_back()
            turn_left(speed)

        else:  # else the touch sensor is not pressed or not configured, so set the speed to 0
            speed = 30
            move_forward(speed)

        time.sleep(0.02)

except KeyboardInterrupt:
    BP.reset_all()
