import random
from time import perf_counter

from context_managers import rand_state
from year_1.contest3_spring_2024.e import process_test


class TestE:
    def test_example_1(self):
        n = 3
        numbers = [
            '112',
            '33325999',
            '11225426'
        ]
        assert process_test(numbers) == "no", "WA on example test 1"

    def test_example_2(self):
        n = 5
        numbers = [
            '113',
            '12340',
            '123440',
            '12345',
            '98346'
        ]
        assert process_test(numbers) == "yes", "WA on example test 2"

    def test_time(self):
        n = int(1e5)
        with rand_state(42):
            numbers = [''.join([str(random.randrange(0, 10)) for _ in range(10)]) for __ in range(n)]
        start = perf_counter()
        process_test(numbers)
        end = perf_counter()
        assert end - start < 0.5, f"TL on large data: {end - start} seconds"
