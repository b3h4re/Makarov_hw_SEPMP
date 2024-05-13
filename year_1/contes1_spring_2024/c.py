def get_ans(n, m):
    if n * (n - 1) // 2 != m:
        return 'no'

    edges = set()
    for _ in range(m):
        start, end = map(int, input().split())
        if (start, end) in edges or (end, start) in edges:
            return 'no'
        edges.add((start, end))

    return 'yes'


n, m = map(int, input().split())
print(get_ans(n, m))
