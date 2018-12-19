import brickpi3  # import the BrickPi3 drivers
signal = 0
    BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
    BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)

class IR_Sensor:



    def isTooClose():
        if signal < 20:
            return true
        return false
    def update_signal():
        while True:
            signal = BP.get_sensor(BP.PORT_3)
