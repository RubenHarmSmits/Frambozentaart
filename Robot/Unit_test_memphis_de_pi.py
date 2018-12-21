import unittest
import Brick_pi_3


from Memphis_de_pi import Memphis_de_pi
from Touch_sensor import Touch_sensor_class
from IR_Sensor import IR_Sensor
from Engine import Engine


class MyTestCase(unittest.TestCase):

    def __init__(self):
        self.touch_sensor = Touch_sensor_class()
        self.infra_sensor = IR_Sensor()
        self.memphis_de_pi = Memphis_de_pi()

    def test_manage_move_change_state_to_forward(self):
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(None, None, 40)

        brick_pi_3.valueTouch1 = 0
        brick_pi_3.valueIR = 10
        self.memphis_de_pi.manage_move()
        self.assertEqual("forward", self.memphis_de_pi.state)

    def test_manage_move_change_state_to_turn_right(self):
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(1, None, 60)

        # touch_sensor.getSignal(brick_pi_3.valueTouch1)
        # infra_sensor.is_too_close(brick_pi_3.valueIR)
        self.memphis_de_pi.manage_move()
        self.assertEqual("turn right", self.memphis_de_pi.state)

    def test_manage_move_change_state_to_turn_left(self):
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(1, None, 40)

        # touch_sensor.getSignal(brick_pi_3.valueTouch1)
        # infra_sensor.is_too_close(brick_pi_3.valueIR)
        self.memphis_de_pi.manage_move()
        self.assertEqual("turn left", self.memphis_de_pi.state)

if __name__ == '__main__':
    unittest.main()
