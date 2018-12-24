import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
BP.set_sensor_type(BP.PORT_4,BP.SENSOR_TYPE.EV3_COLOR_COLOR)




class Color_sensor_class:
    def __init__(self):
        self.color = None
        self.color_state = None
        self.save_index = int()
        self.color_list = []

    def get_color(self):
        self.color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
        self.value = BP.get_sensor(BP.PORT_4)
        print(self.color[self.value])

    def get_color_pattern(self):
        print("Inside get color pattern")
        self.get_color()
        if not self.save_index:
            self.save_index = 0
        self.color_list[self.save_index] = self.color[self.value]
        print(self.color_list)
        self.save_index = self.save_index + 1
        if self.save_index == 4:
            self.save_index = 0
        self.set_color_pattern_state()

    def set_color_pattern_state(self):
        # print("Inside set color pattern state")
        if self.color_list == ["Blue", "Black", "Red"]:
            print("end of wip")
            self.color_state = "end of wip"
        else:
            self.color_state = "normal"

