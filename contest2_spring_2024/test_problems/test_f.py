from contest2_spring_2024.f import process_test
from test_data.test_data_f import TestDataF


class TestF:
    def test_correct_answer_1(self):
        rows, cols, cut = TestDataF.rows_cols_cut_1
        inp = TestDataF.inp_1
        ans = TestDataF.ans_1
        assert ans == process_test(rows, cols, inp, cut), "Wrong Answer"

    def test_correct_answer_2(self):
        rows, cols, cut = TestDataF.rows_cols_cut_2
        inp = TestDataF.inp_2
        ans = TestDataF.ans_2
        assert ans == process_test(rows, cols, inp, cut), "Wrong Answer"

    def test_correct_answer_3(self):
        rows, cols, cut = TestDataF.rows_cols_cut_3
        inp = TestDataF.inp_3
        ans = TestDataF.ans_3
        assert ans == process_test(rows, cols, inp, cut), "Wrong Answer"