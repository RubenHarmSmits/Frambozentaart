import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_4,BP.SENSOR_TYPE.EV3_COLOR_COLOR)




class Color_sensor_class:
    def __init__(self):
        self.color = None


    def get_color(self):
        self.color = ["Black", "Red"]
        return self.color[BP.get_sensor(BP.PORT_4)]