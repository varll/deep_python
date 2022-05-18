import unittest
from descriptor import Data


class TestDescriptor(unittest.TestCase):
    def test_creation(self):
        test_data = Data(0, 'test', 0)
        self.assertEqual(test_data.num, 0)
        self.assertEqual(test_data.name, 'test')
        self.assertEqual(test_data.price, 0)

    def test_num(self):
        with self.assertRaises(TypeError):
            Data(9.2, 'test', 0)
        with self.assertRaises(TypeError):
            Data('', 'test', 3)

    def test_name(self):
        with self.assertRaises(TypeError):
            Data(0, 0, 0)
        with self.assertRaises(TypeError):
            Data(0, 8.9, 0)

    def test_price(self):
        with self.assertRaises(TypeError):
            Data(0, 'test', 9.9)
        with self.assertRaises(ValueError):
            Data(0, 'test', -3)


if __name__ == '__main__':
    unittest.main()
