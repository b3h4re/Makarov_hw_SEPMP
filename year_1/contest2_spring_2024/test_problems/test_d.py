from year_1.contest2_spring_2024.d import process_test
from test_data.test_data_d import TestDataD


class TestD:
    def test_correct_answers(self):
        inputs = TestDataD.inputs
        correct_outputs = TestDataD.outputs
        outputs = []
        for i in range(len(inputs)):
            inp = inputs[i].split("\n")
            res = []
            t = int(inp[0])
            line = 1
            for _ in range(t):
                s, p = map(int, inp[line].split())
                line += 1
                arr = []
                for j in range(p):
                    arr.append(tuple(map(int, inp[line].split())))
                    line += 1
                process_test(s, arr, res)
            outputs.append("\n".join(res))
            assert outputs[i] == correct_outputs[i]
