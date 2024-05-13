import random
from time import perf_counter

from year_1.contest3_spring_2024.b import get_power
from context_managers import rand_state


class TestB:
    def test_example(self):
        inputs = [
            'abcd',
            'aaaa',
            'ababab'
        ]
        answers = [
            1,
            4,
            3,
        ]
        for t in range(3):
            assert get_power(inputs[t]) == answers[t], f"Wrong answer on example test {t+1}"

    def test_time(self):
        with rand_state(42):
            string = ''.join([chr(random.randrange(97, 122+1)) for _ in range(int(1e6))])

        start = perf_counter()
        ans = get_power(string)
        end = perf_counter()
        assert end - start < 0.5, "TL"
