import unittest
from descriptor import Data, Integer, String, PositiveInteger


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

    def test_change_val(self):
        test_data = Data(0, 'test', 0)

        test_data.num = 4
        self.assertEqual(test_data.num, 4)
        with self.assertRaises(TypeError):
            test_data.num = 'test'
        self.assertEqual(test_data.num, 4)

        test_data.name = 'test'
        self.assertEqual(test_data.name, 'test')
        with self.assertRaises(TypeError):
            test_data.name = -1
        self.assertEqual(test_data.name, 'test')

        test_data.price = 25
        self.assertEqual(test_data.price, 25)
        with self.assertRaises(ValueError):
            test_data.price = -1
        self.assertEqual(test_data.price, 25)


if __name__ == '__main__':
    unittest.main()
