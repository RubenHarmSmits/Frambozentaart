import brickpi3  # import the BrickPi3 drivers

class Touch_sensor_class:
    def __init__(self):
        self.signal = False

    def get_signal(self):
        return self.signal