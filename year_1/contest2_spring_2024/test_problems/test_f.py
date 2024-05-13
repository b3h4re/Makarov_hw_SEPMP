import random

from year_1.contest2_spring_2024.f import process_test
from year_1.contest2_spring_2024.f_slow import process_test as get_correct_ans
from context_managers import rand_state
from test_data.test_data_f import TestDataF
from time import perf_counter


class TestF:
    def test_f(self):
        for i in range(len(TestDataF.rows_cols_cut_data)):
            rows, cols, cut = TestDataF.rows_cols_cut_data[i]
            inp = TestDataF.input_data[i]
            ans = TestDataF.answers[i]
            assert ans == process_test(rows, cols, inp, cut), f"Wrong Answer for test {i + 1}"

    def test_f_time(self):
        rows, cols = 300, 300
        tmp = []
        for i in range(rows):
            tmp.append(str(i))
            tmp.append(str(i))
        cut = len(tmp) // 2
        inp = ' '.join(tmp)
        ans = min(rows, cols)
        max_time = 1
        start = perf_counter()
        result = process_test(rows, cols, inp, cut)
        end = perf_counter()
        assert end - start < max_time, f"Program took {end - start} seconds!"

    @staticmethod
    def _get_fields():
        coordinates = {
            0: (0, 0), 1: (0, 1), 2: (0, 2),
            3: (1, 0), 4: (1, 1), 5: (1, 2),
            6: (2, 0), 7: (2, 1), 8: (2, 2),
            9: (3, 0), 10: (3, 1), 11: (3, 2)
        }
        power = 12
        for x in range(2 ** power):
            cuts = bin(x)[2:].zfill(power)
            cuts_coordinates = ''
            for i in range(power):
                if cuts[i] == '1':
                    xi, yi = coordinates[i]
                    if len(cuts_coordinates) > 0:
                        cuts_coordinates += ' '
                    cuts_coordinates += str(xi) + ' ' + str(yi)
            yield cuts_coordinates

    @staticmethod
    def _get_placements(rows, cols, cuts, placed):
        for i in range(rows):
            for j in range(cols):
                if (i, j) in cuts:
                    continue
                for x, y in placed:
                    if x == i or y == j:
                        break
                else:
                    yield i, j

    def _get_solution_slow(self, rows, cols, cuts, placed):
        placements = list(self._get_placements(rows, cols, cuts, placed))
        if len(placements) == 0:
            return len(placed)
        rt = -1
        for p in placements:
            rt = max(rt, self._get_solution_slow(rows, cols, cuts, placed + [p]))
        return rt

    def test_f_4_3(self):
        for cut_input in self._get_fields():
            tmp = list(map(int, cut_input.split()))
            cuts = set([(tmp[i], tmp[i + 1]) for i in range(0, len(tmp), 2)])
            ans = self._get_solution_slow(4, 3, cuts, [])
            assert ans == process_test(4, 3, cut_input, len(cuts)), \
                f"1\n4 3 {len(cuts)}\n{cut_input}"

    def test_big_field(self):
        inp = ''
        rows, cols = 300, 300
        all_coordinates = []
        for i in range(rows):
            for j in range(cols):
                all_coordinates.append((i, j))
        with rand_state(42):
            cut = random.randrange(int((rows * cols) ** 0.5), rows * cols)
            random.shuffle(all_coordinates)
            for i in range(cut):
                inp += str(all_coordinates[i][0]) + ' ' + str(all_coordinates[i][1])
                if i < cut:
                    inp += ' '
        assert get_correct_ans(rows, cols, inp, cut) == process_test(rows, cols, inp, cut), "WA on large test."
