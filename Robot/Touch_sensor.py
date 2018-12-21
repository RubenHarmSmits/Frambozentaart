import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_1,BP.SENSOR_TYPE.TOUCH)


class Touch_sensor_class:
    def __init__(self, port):
        self.signal = 0
        self.port = port

    def get_signal(self):
        if self.port ==1:
            self.signal = BP.get_sensor(BP.PORT_1)
            print("FRONT-Touch signal: %s" % (str(self.signal)))
            return self.signal
        elif self.port ==2:
            self.signal = BP.get_sensor(BP.PORT_2)
            print("WIP-Touch signal: %s" % (str(self.signal)))
            return self.signal
