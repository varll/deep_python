import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.test_list1 = CustomList([1, 2, 3])
        self.test_list2 = CustomList([3, 4])
        self.test_list3 = CustomList([3, 2, 1])
        self.test_empty_list = CustomList()

    def test_add(self):
        self.assertEqual(list(self.test_list1 + self.test_list2), [4, 6, 3])
        self.assertEqual(list(self.test_list1), [1, 2, 3])
        self.assertEqual(list(self.test_list2), [3, 4])

        self.assertEqual(list(self.test_list1 + [1]), [2, 2, 3])
        self.assertEqual(list(self.test_list1), [1, 2, 3])

        self.assertEqual(list([1, 2] + self.test_list1), [2, 4, 3])
        self.assertEqual(list(self.test_list1), [1, 2, 3])

        self.assertEqual(list(self.test_list1 + []), [1, 2, 3])
        self.assertEqual(list(self.test_list1 + self.test_empty_list), [1, 2, 3])

    def test_sub(self):
        self.assertEqual(list(self.test_list1 - self.test_list2), [-2, -2, 3])
        self.assertEqual(list(self.test_list1), [1, 2, 3])
        self.assertEqual(list(self.test_list2), [3, 4])

        self.assertEqual(list(self.test_list1 - [1]), [0, 2, 3])
        self.assertEqual(list(self.test_list1), [1, 2, 3])

        self.assertEqual(list([1, 2] - self.test_list1), [0, 0, -3])
        self.assertEqual(list(self.test_list1), [1, 2, 3])

        self.assertEqual(list(self.test_list1 - []), [1, 2, 3])
        self.assertEqual(list(self.test_list1 - self.test_empty_list), [1, 2, 3])

    def test_type(self):
        self.assertEqual(type(self.test_list1 + self.test_list2), CustomList)
        self.assertEqual(type(self.test_list1 + []), CustomList)
        self.assertEqual(type([1, 3, 8] + self.test_list1), CustomList)

        self.assertEqual(type(self.test_list1 - self.test_list2), CustomList)
        self.assertEqual(type(self.test_list1 - []), CustomList)
        self.assertEqual(type([1, 3, 8] - self.test_list1), CustomList)

    def test_eq(self):
        self.assertTrue(self.test_list1 == self.test_list1)
        self.assertTrue(self.test_list1 == [1, 2, 3])
        self.assertTrue(self.test_list1 == self.test_list3)
        self.assertTrue([1, 2, 3] == self.test_list1)
        self.assertTrue(self.test_empty_list == [])

    def test_ne(self):
        self.assertTrue(self.test_list1 != self.test_list2)
        self.assertTrue(self.test_list1 != [5, 5, 5])
        self.assertTrue([] != self.test_list1)
        self.assertTrue(self.test_empty_list != [1])

    def test_gt(self):
        self.assertTrue(self.test_list2 > self.test_empty_list)
        self.assertTrue(self.test_list1 > [])
        self.assertTrue([3, 3, 3, 3, 3] > self.test_list1)

    def test_lt(self):
        self.assertTrue(self.test_list1 < self.test_list2)
        self.assertTrue([] < self.test_list1)
        self.assertTrue([3] < self.test_list1)

    def test_le(self):
        self.assertTrue(self.test_list1 <= self.test_list2)
        self.assertTrue([] <= self.test_list1)
        self.assertTrue([3, 2, 1] <= self.test_list1)

    def test_ge(self):
        self.assertTrue(self.test_list2 >= self.test_empty_list)
        self.assertTrue(self.test_list1 >= [])
        self.assertTrue([3, 3, 3, 3, 3] >= self.test_list1)


if __name__ == "__main__":
    unittest.main()
