import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_get_null_val(self):
        cache = LRUCache(4)

        self.assertEqual(cache.get('test'), None)

    def test_set_and_get(self):
        cache = LRUCache(3)

        cache.set('k1', 'val1')
        cache.set('k2', 'val2')
        cache.set('k3', 'val3')

        self.assertEqual(cache.get('k1'), 'val1')
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertEqual(cache.get('k3'), 'val3')

    def test_set_twice(self):
        cache = LRUCache(2)

        cache.set('k1', 'test_val1')
        cache.set('k1', 'true_val1')

        self.assertEqual(cache.get('k1'), 'true_val1')

    def test_from_hw(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get('k3'), None)
        self.assertEqual(cache.get('k2'), 'val2')
        self.assertEqual(cache.get('k1'), 'val1')

        cache.set('k3', 'val3')

        self.assertEqual(cache.get('k3'), 'val3')
        self.assertEqual(cache.get('k2'), None)
        self.assertEqual(cache.get('k1'), 'val1')


if __name__ == '__main__':
    unittest.main()
