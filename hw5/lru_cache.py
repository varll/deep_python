from collections import deque


class LRUCache:

    def __init__(self, limit=42):
        self.lru_cache = deque()
        self.limit = limit

    def find(self, key):
        for i in range(len(self.lru_cache)):
            if self.lru_cache[i][0] == key:
                return i

        return -1

    def get(self, key):
        idx = self.find(key)
        if idx != -1:
            k, v = self.lru_cache[idx]
            del self.lru_cache[idx]
            self.lru_cache.append((k, v))
            return v

        return None

    def set(self, key, value):
        idx = self.find(key)
        if idx != -1:
            del self.lru_cache[idx]
            self.lru_cache.append((key, value))
        else:
            if len(self.lru_cache) >= self.limit:
                self.lru_cache.popleft()
            self.lru_cache.append((key, value))

    def __str__(self):
        return f'{self.lru_cache}'
