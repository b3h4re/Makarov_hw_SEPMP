import random

from year_1.contest3_spring_2024.a import process_test
from time import perf_counter

from context_managers import rand_state


class TestA:
    def test_example_input(self):
        ans_given = list(process_test(5, 'aabaa'))
        correct_ans = [1, 2, 0, 1, 5]
        assert correct_ans == ans_given, "Incorrect answer to example test."

    def test_large_input(self):
        for seed in [42, 2134, 34]:
            with rand_state(seed):
                n = 200_000
                string = ''
                for _ in range(n):
                    char = chr(random.randrange(97, 122+1))
                    string += char
                start_time = perf_counter()
                process_test(n, string)
                end_time = perf_counter()
                assert end_time - start_time < 0.501, f"Program taking too long: {end_time - start_time} seconds"
