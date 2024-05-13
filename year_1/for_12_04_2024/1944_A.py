def get_ans(vertices, can_destroy):
    if vertices == 1:
        return 1
    if can_destroy == 0:
        return vertices

    res = vertices

    rem = 0
    rem_max = 0

    for x in range(vertices-1, 0, -1):
        rem += x - (vertices - x - 1)
        rem_max += x

        if rem <= can_destroy <= rem_max:
            res = x

    return res


if __name__ == '__main__':
    t = int(input())

    for test in range(1, t+1):
        n, k = map(int, input().split())
        print(get_ans(n, k))