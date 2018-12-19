
from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

import time  # import the time library for the sleep function
import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_1,
                   BP.SENSOR_TYPE.TOUCH)  # Configure for a touch sensor. If an EV3 touch sensor is connected, it will be configured for EV3 touch, otherwise it'll configured for NXT touch.

try:
    print("Press touch sensor on port 1 to run motors")
    value = 0
    while not value:
        try:
            print("First loop: before get_sensor ")
            value = BP.get_sensor(BP.PORT_1)
            print("First loop: after get_sensor ")
        except brickpi3.SensorError:
            pass

    speed = 30
    adder = 1
    while True:
        print("Second loop: before get_sensor ")
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns the sensor value.
        # try:
        value = BP.get_sensor(BP.PORT_1)
        print("Second loop: after get_sensor ")
        # except brickpi3.SensorError as error:
        #     print(error)
        #     value = 0

        if value:  # if the touch sensor is pressed
            speed = 0
            print("Third - if then: set speed 0 ")
            # if speed <= -100 or speed >= 100:  # if speed reached 100, start ramping down. If speed reached -100, start ramping up.
            #     adder = -adder
            # speed += adder
        else:  # else the touch sensor is not pressed or not configured, so set the speed to 0
            speed = 30
            print("Third - if then: set speed 30 ")
            # speed = 0
            # adder = 1

        # Set the motor speed for all four motors
        BP.set_motor_power(BP.PORT_A + BP.PORT_D, speed)
        print("MOTOR POWER ON")

        # try:
        #     # Each of the following BP.get_motor_encoder functions returns the encoder value (what we want to display).
        #     print("Encoder A: %6d  B: %6d  C: %6d  D: %6d" % (
        #     BP.get_motor_encoder(BP.PORT_A), BP.get_motor_encoder(BP.PORT_B), BP.get_motor_encoder(BP.PORT_C),
        #     BP.get_motor_encoder(BP.PORT_D)))
        # except IOError as error:
        #     print(error)

        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
