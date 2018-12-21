import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)

class IR_sensor_class:

    def __init__(self):
        self.signal = 0

    def isTooClose(self):
        self.update_signal()
        if self.signal < 70:
            print("Infra signal: %s" % (str(self.signal)))
            return True
        elif self.signal > 69:
            print("Infra signal: %s" % (str(self.signal)))
            return False


    # def average_IR_to_far(self):
    #     sum_distance = 0
    #     for i in range(5):
    #         distance = BP.get_sensor(BP.PORT_3)
    #         sum_distance += distance
    #     if sum_distance/5>=80:
    #         return True
    #     return False
    #
    # def average_IR_to_far(self):
    #     sum_distance = 0
    #
    #     for i in range(5):
    #         self.update_signal()
    #         distance = self.signal
    #         sum_distance += distance
    #
    #     if sum_distance / 5 >= 80:
    #         return True
    #     else:
    #         return False

    def average_IR_to_far(self):
        sum_distance = 0
        
        for i in range(5):
            self.update_signal()
            distance = self.signal
            sum_distance += distance
        if sum_distance/5>=80:
            return True
        else:
            return False



    def update_signal(self):
        self.signal = BP.get_sensor(BP.PORT_3)

