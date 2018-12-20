import unittest
import Brick_pi_3
import Memphis_de_pi

class MyTestCase(unittest.TestCase):
    def test_manage_move_change_state_to_forward(self):
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(None, None, 40)
        touch_sensor = Touch_sensor.Touch_sensor_class()
        infra_sensor = Infra_sensor.Infra_sensor_class()
        memphis_de_pi = Memphis_de_pi.Memphis_de_pi_class()

        touch_sensor.getSignal(brick_pi_3.valueTouch1)
        infra_sensor.is_too_close(brick_pi_3.valueIR)
        memphis_de_pi.manage_move()
        self.assertEqual("forward", memphis_de_pi.state)

    def test_manage_move_change_state_to_turn_right(self):
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(1, None, 60)
        touch_sensor = Touch_sensor.Touch_sensor_class()
        infra_sensor = Infra_sensor.Infra_sensor_class()
        memphis_de_pi = Memphis_de_pi.Memphis_de_pi_class()

        touch_sensor.getSignal(brick_pi_3.valueTouch1)
        infra_sensor.is_too_close(brick_pi_3.valueIR)
        memphis_de_pi.manage_move()
        self.assertEqual("turn right", memphis_de_pi.state)

    def test_manage_move_change_state_to_turn_left(self):
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(1, None, 40)
        touch_sensor = Touch_sensor.Touch_sensor_class()
        infra_sensor = Infra_sensor.Infra_sensor_class()
        memphis_de_pi = Memphis_de_pi.Memphis_de_pi_class()

        touch_sensor.getSignal(brick_pi_3.valueTouch1)
        infra_sensor.is_too_close(brick_pi_3.valueIR)
        memphis_de_pi.manage_move()
        self.assertEqual("turn left", memphis_de_pi.state)

if __name__ == '__main__':
    unittest.main()
