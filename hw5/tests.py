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

    def test_single_element(self):
        cache = LRUCache(1)

        cache.set('k1', 'val1')
        self.assertEqual(cache.get('k1'), 'val1')

        cache.set('k2', 'val2')

        self.assertEqual(cache.get('k1'), None)
        self.assertEqual(cache.get('k2'), 'val2')

    def test_complete_exclusion(self):
        cache = LRUCache(3)

        for i in range(6):
            cache.set(f'k{i+1}', f'val{i+1}')

        for i in range(3):
            self.assertEqual(cache.get(f'k{i+1}'), None)

        for i in range(3):
            self.assertEqual(cache.get(f'k{i+4}'), f'val{i+4}')

    def test_set_twice_and_exclusion(self):
        cache = LRUCache(5)

        for i in range(5):
            cache.set(f'k{i+1}', f'val{i+1}')

        cache.set('k1', 'val1')

        for i in range(4):
            cache.set(f'test_k{i+1}', f'test_val{i+1}')

        self.assertEqual(cache.get('k1'), 'val1')
        for i in range(4):
            self.assertEqual(cache.get(f'k{i+2}'), None)
        for i in range(4):
            self.assertEqual(cache.get(f'test_k{i+1}'), f'test_val{i+1}')


if __name__ == '__main__':
    unittest.main()
