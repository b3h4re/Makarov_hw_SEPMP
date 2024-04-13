from collections import deque
from heapq import heappush


def get_parent(x):
    if x % 2 == 1:
        return (x - 1) // 2
    return (x - 2) // 2


def calc_bigger(heap, elem):
    res = 0
    q = deque()
    used = set()
    for i in range(len(heap)-1, -1, -1):
        if 2*i + 1 < len(heap):
            break
        parent = get_parent(i)
        if elem < heap[i]:
            res += 1
            if parent >= 0 and parent not in used:
                q.append(parent)
                used.add(parent)

    while len(q) > 0:
        v = q.popleft()
        parent = get_parent(v)
        if elem < heap[v]:
            res += 1
            if parent >= 0 and parent not in used:
                q.append(parent)
                used.add(parent)
    return res


t = int(input())

for test in range(1, t+1):
    n = int(input())
    ladder = list(map(int, input().split()))

    heap = [ladder[-1]]
    res = 0
    for i in range(n-2, -1, -1):
        bigger = calc_bigger(heap, ladder[i])
        res += ladder[i] * bigger
        heappush(heap, ladder[i])

    print(res)