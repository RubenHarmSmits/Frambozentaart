import unittest
import Brick_pi_3
import Infra_sensor

class Unit_test_infra_sensor_class(unittest.TestCase):
    def test_BP_IR_too_close(self):
        infra_sensor = Infra_sensor.Infra_sensor_class()
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(None, None, 40)
        self.assertEqual(False, infra_sensor.is_too_close(brick_pi_3.valueIR))

    def test_BPIR_too_far(self):
        infra_sensor = Infra_sensor.Infra_sensor_class()
        brick_pi_3 = Brick_pi_3.Brick_pi_3_class(None, None, 60)
        self.assertEqual(True, infra_sensor.is_too_close(brick_pi_3.valueIR))

if __name__ == '__main__':
    unittest.main()
