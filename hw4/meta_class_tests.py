import unittest
from meta_class import CustomClass


class TestCustomClass(unittest.TestCase):
    def setUp(self):
        self.inst = CustomClass()

    def test_x(self):
        self.assertEqual(CustomClass.custom_x, 50)
        self.assertEqual(self.inst.custom_x, 50)
        with self.assertRaises(AttributeError):
            CustomClass.x
        with self.assertRaises(AttributeError):
            self.inst.x

    def test_val(self):
        self.assertEqual(self.inst.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.inst.val

    def test_line(self):
        self.assertEqual(self.inst.custom_line(), 100)
        self.assertEqual(CustomClass.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.inst.line()
        with self.assertRaises(AttributeError):
            CustomClass.line()

    def test_str(self):
        self.assertEqual(str(self.inst), "Custom_by_metaclass")

    def test_dynamic(self):
        self.inst.dynamic = 'added later'

        self.assertEqual(self.inst.custom_dynamic, 'added later')
        with self.assertRaises(AttributeError):
            self.inst.dynamic

    def test_custom_setattr(self):
        self.inst.__setattr__('test', 14)

        self.assertEqual(self.inst.custom_test, 14)
        with self.assertRaises(AttributeError):
            self.inst.test


if __name__ == "__main__":
    unittest.main()
