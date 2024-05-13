import random
from time import perf_counter

from context_managers import rand_state
from year_1.contest3_spring_2024.c import find_password


class TestC:
    def test_example(self):
        tests = [
            (3, "baababacb", "aba"),
            (2, "ababa", "ab")
        ]
        for n, string, ans in tests:
            assert find_password(n, string) == ans, f"WA on example test {n}, \'{string}\'"

    def test_time(self):
        n = 10
        with rand_state(69420):
            string = ''.join([chr(random.randrange(ord('a'), ord('z')+1)) for __ in range(int(1e5))])
        start = perf_counter()
        find_password(n, string)
        end = perf_counter()
        assert end - start < 1, "TL on large test"
