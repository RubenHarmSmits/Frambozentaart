import unittest
import Engine

class Unit_test_TouchSensor (unittest.TestCase):
    def test_engine_change_speed_positive(self):
        engine = Engine.Engine_class()

        engine.change_speed(50)
        self.assertEqual(50, engine.speed)

    def test_engine_change_speed_negative(self):
        engine = Engine.Engine_class()

        engine.change_speed(-50)
        self.assertEqual(-50, engine.speed)

if __name__ == '__main__':
    unittest.main()
