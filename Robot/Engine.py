import brickpi3  # import the BrickPi3 drivers
import time

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.


class Engine:

    def __init__(self, port):
        self.speed = 0
        if port == 1:
            BP.set_motor_power(BP.PORT_A, self.speed)
            self.portcode = BP.PORT_A
        else:
            BP.set_motor_power(BP.PORT_D, self.speed)
            self.portcode = BP.PORT_D

    def change_speed(self, target_speed):
        # print("Changing speed in engine ")
        self.speed = target_speed
        BP.set_motor_power(self.portcode, self.speed)

    def change_speed_dps(self, target_speed_dps):
        self.speed = target_speed_dps
        BP.set_motor_dps(self.portcode, self.speed)


