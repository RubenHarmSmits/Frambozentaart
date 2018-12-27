import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_4,BP.SENSOR_TYPE.EV3_COLOR_COLOR)


class Color_sensor_class:
    def __init__(self):
        self.color = None
        self.color_state = None
        self.save_index = int()
        self.color_list = [0, 0]

    def get_color(self):
        self.color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
        self.value = BP.get_sensor(BP.PORT_4)
        print(self.color[self.value])
        return self.color[self.value]

    def set_color_state(self):
        print("Inside get color pattern")
        self.get_color()
        if self.color[self.value] == "Brown":
            print("end of wip")
            self.color_state = "end of wip"
        else:
            self.color_state = "normal"

    def end_quadrant_check(self):
        self.value = BP.get_sensor(BP.PORT_4)
        if self.color[self.value] == "Black":
            self.color_list[0] = self.color[self.value]
            return False
        elif self.color_list[0] == "Black" and self.color[self.value] == "Red":
            self.color_list[1] = self.color[self.value]
            return True
        else:
            self.color_list[0] = 0
            self.color_list[1] = 0
        return False

