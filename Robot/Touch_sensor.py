import brickpi3  # import the BrickPi3 drivers
BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_1,BP.SENSOR_TYPE.TOUCH)


class Touch_sensor_class:
    def __init__(self):
        self.signal = 0

    def get_signal(self):
        self.signal = BP.get_sensor(BP.PORT_1)
        print("Touch signal: %s" % (str(self.signal)))
        return self.signal

