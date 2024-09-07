def process_test(numbers):
    bor = [[-1] * 10 + [None]]
    for i in range(len(numbers)):
        j = 0
        for u in range(len(numbers[i])):
            x = numbers[i][u]
            if bor[j][-1] is not None:
                return "no"
            if bor[j][int(x)] == -1:
                bor[j][int(x)] = len(bor)
                j = len(bor)
                bor.append([-1] * 10 + [None])
            else:
                j = bor[j][int(x)]
        bor[j][-1] = i

        for u in range(10):
            if bor[j][u] != -1:
                return "no"

    return "yes"


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t+1):
        n_ = int(input())
        numbers_ = [input() for _ in range(n_)]
        print(process_test(numbers_))
