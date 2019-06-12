# Implement Set that have sample function.
# All methods should work for O(1).
import random
from unittest import TestCase


class SampleseableSet:
    def __str__(self):
        s = '(' + ', '.join(str(elem) for elem in self.map_1.keys()) + ')'
        return f'set: {s}\n' \
            f'map_1: {self.map_1}\n' \
            f'map_2: {self.map_2}\n' \
            f'current: {self.current}'

    def __init__(self):
        self.map_1 = dict()
        self.map_2 = dict()
        self.current = 0

    def insert(self, val):
        if val not in self.map_1:
            self.map_1[val] = self.current
            self.map_2[self.current] = val
            self.current += 1

    def remove(self, val):
        if val in self.map_1:
            self.current -= 1
            self.map_2[self.map_1[val]] = self.map_2[self.current]
            self.map_1[self.map_2[self.current]] = self.map_1[val]
            del self.map_1[val]
            del self.map_2[self.current]

    def contains(self, val):
        return val in self.map_1

    def sample(self):
        """
        Returns any element with equal chances
        """
        r = random.randint(0, self.current - 1)
        return self.map_2[r]


class TestSampleseableSet(TestCase):
    def test_insert(self):
        s = SampleseableSet()
        s.insert(3)
        s.insert(1)
        s.insert(7)

        print(s)

    def test_remove(self):
        s = SampleseableSet()
        s.insert(1)
        s.insert(2)
        s.insert(3)
        s.insert(4)
        s.insert(5)

        s.remove(4)
        s.remove(1)

        print(s)

    def test_contains(self):
        s = SampleseableSet()
        s.insert(1)
        s.insert(2)
        s.insert(3)
        s.insert(4)
        s.insert(5)

        self.assertTrue(s.contains(1))
        self.assertTrue(s.contains(4))

        self.assertFalse(s.contains(10))

        print(s)

    def test_sample(self):
        s = SampleseableSet()
        s.insert(1)
        s.insert(2)

        print(s)

        count_1 = 0
        count_2 = 0
        for i in range(100):
            ss = s.sample()
            if ss == 1:
                count_1 += 1
            elif ss == 2:
                count_2 += 1
            else:
                raise RuntimeError('wrong sample!')

        print(f'count_1: {count_1}')
        print(f'count_2: {count_2}')
