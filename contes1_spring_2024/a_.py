from collections import deque


def bfs(g):
    q = deque()
    q.append(0)
    links = [False] * n
    pending = [False] * n
    pending[0] = True
    res = 0

    while len(q) > 0:
        vertex = q.popleft()

        if links[vertex]:
            continue
        links[vertex] = True

        for i in range(vertex + 1, len(g)):
            if g[i] > g[vertex]:
                res += g[vertex]
                if not links[i] and not pending[i]:
                    q.append(i)
                    pending[i] = True
            elif not pending[i]:
                q.append(i)
                pending[i] = True
    return res


t = int(input())

for _ in range(t):
    n = int(input())
    ladder = list(map(int, input().split()))
    memo = [0] * (n + 2)
    memo[-2] = n - 1
    memo[-1] = 0

    print(bfs(ladder))