from collections import deque
from heapq import heappush
import threading


def bfs(g, start, ans, elem):
    if elem > - g[start]:
        return ans
    ans += g[start]
    q = deque()
    q.append(start)
    while len(q) > 0:
        v = q.popleft()
        for child in [2*v + 1, 2*v + 2]:
            if child < len(g) and elem <= - g[child]:
                ans += g[child]
                q.append(child)
    return ans


def get_ans(number, n, ladder):
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
    ans.append((number, res))


t = int(input())

ans = []
for i in range(t):
    n = int(input())
    ladder = list(map(int, input().split()))
    thread = threading.Thread(target=get_ans, args=(i, n, ladder))
    thread.start()
ans.sort(key=(lambda x: x[0]))
for _, e in ans:
    print(e)