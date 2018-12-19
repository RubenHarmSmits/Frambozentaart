#import brickpi3  # import the BrickPi3 drivers
#BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.


class Engine:


    def __init__(self):
        self.speed = 0
#        BP.set_motor_power(BP.PORT_A, speed)

    def change_speed(self, target_speed):
        self.speed = target_speed