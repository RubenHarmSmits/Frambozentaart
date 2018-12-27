import brickpi3  # import the BrickPi3 drivers
import time  # import the time library for the sleep function

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)

class IR_sensor_class:

    def __init__(self):
        self.signal = 0
        self.signal_list = [0, 0, 0, 0, 0]
        self.save_index = 0
        self.current_average = 10

    def isTooClose(self):
        self.update_signal()
        if self.signal < 45:
            print("Infra signal: %s" % (str(self.signal)))
            return True
        elif self.signal > 44:
            print("Infra signal: %s" % (str(self.signal)))
            return False

    def save_signal(self):
        self.update_signal()
        self.signal_list[self.save_index] = self.signal
        self.save_index = self.save_index + 1
        if self.save_index == 5:
            self.save_index = 0

    def average_signal(self):
        self.save_signal()
        self.current_average = sum(self.signal_list)/len(self.signal_list)
        print("Average IR values: %s" % (str(self.current_average)))

    def update_signal(self):
        if BP.get_sensor(BP.PORT_3) < 100:
            self.signal = BP.get_sensor(BP.PORT_3)

    # def average_IR_to_far(self):
    #     sum_distance = 0
    #
    #     for i in range(5):
    #         self.update_signal()
    #         time.sleep(0.02)
    #         print("Infra signal: %s" % (str(self.signal)))
    #         distance = self.signal
    #         sum_distance = distance + sum_distance
    #         print("Sum_distance: %s" % (str(sum_distance)))
    #
    #     if sum_distance / 5 >= 40:
    #         return True
    #     else:
    #         return False