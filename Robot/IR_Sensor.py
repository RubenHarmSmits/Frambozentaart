import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)

class IR_Sensor:

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

    def update_signal(self):
        self.signal = BP.get_sensor(BP.PORT_3)

