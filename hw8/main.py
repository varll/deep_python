import cProfile
import pstats
import io
import weakref
from memory_profiler import profile
from lru_cache import LRUCache


class ValueDefault:
    def __init__(self, a):
        self.a = a
        self.b = 'test'
        self.c = [i for i in range(20)]
        self.d = {i: i**2 for i in range(20)}


class ValueSlot:
    __slots__ = ('a', 'b', 'c', 'd')

    def __init__(self, a):
        self.a = a
        self.b = 'test'
        self.c = [i for i in range(20)]
        self.d = {i: i**2 for i in range(20)}


def make():
    lru_cache_default = LRUCache(10000)
    for i in range(10000):
        lru_cache_default.set(f'k{i}', ValueDefault(i))

    lru_cache_slot = LRUCache(10000)
    for i in range(10000):
        lru_cache_slot.set(f'k{i}', ValueSlot(i))

    lru_cache_weak_ref = LRUCache(10000)
    for i in range(10000):
        test = ValueDefault(i)
        ref = weakref.ref(test)
        lru_cache_weak_ref.set(f'k{i}', ref)


pr = cProfile.Profile()
pr.enable()

make()

pr.disable()


out = io.StringIO()

ps = pstats.Stats(pr, stream=out)
ps.print_stats()

print(out.getvalue())
