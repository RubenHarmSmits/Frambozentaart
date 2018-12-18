import unittest
import Mock

# https://forum.dexterindustries.com/t/brickpi-module-in-windows-10/3316/3

class MyTestCase(unittest.TestCase):
    def test_something(self):
        mock = Mock(None)
        self.assertEquals(None, mock.value)

    def test_DrukSensorIngedruktChangesBooleanIngedruktNaarTrue(self):
        druk1 = Druk()
        mock = Mock(1)
        druk1.Druk(mock.value)
        self.assertEquals(True, druk1.ingedrukt)


if __name__ == '__main__':
    unittest.main()
