from collections import deque
from heapq import heappush


def bfs(g, start, ans, elem):
    if elem > - g[start]:
        return ans
    ans += g[start]
    q = deque()
    q.append(start)
    while len(q) > 0:
        v = q.popleft()
        for child in [2*v + 1, 2*v + 2]:
            if child < len(g):
                if elem <= - g[child]:
                    ans += g[child]
                    q.append(child)
    return ans


t = int(input())

for test in range(1, t+1):
    n = int(input())
    ladder = list(map(int, input().split()))

    heap = [-ladder[0]]
    s = ladder[0]
    res = 0
    mx = ladder[0]
    mn = ladder[0]

    for i in range(1, n):
        if ladder[i] > mx:
            mx = ladder[i]
            res += s
            heappush(heap, -ladder[i])
        elif ladder[i] < mn:
            mn = ladder[i]
            heap.append(-ladder[i])
        else:
            res += bfs(heap, 0, s, ladder[i])
            heappush(heap, -ladder[i])
        s += ladder[i]
    print(res)