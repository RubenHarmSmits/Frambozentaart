import unittest
import Brick_pi_3
import Touch_sensor

class Unit_test_TouchSensor (unittest.TestCase):
    def test_BP_get_signal_pressed(self):
        touch_sensor = Touch_sensor.Touch_sensor_class()
        bp3 = Brick_pi_3.Brick_pi_3_class(1)
        self.assertEqual(1, touch_sensor.getSignal(bp3.valueTouch1))

    def test_BP_get_signal_not_pressed(self):
        touch_sensor = Touch_sensor.Touch_sensor_class()
        bp3 = Brick_pi_3.Brick_pi_3_class(0)
        self.assertEqual(0, touch_sensor.getSignal(bp3.valueTouch1))

if __name__ == '__main__':
    unittest.main()
