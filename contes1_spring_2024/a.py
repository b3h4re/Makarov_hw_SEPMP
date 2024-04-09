from heapq import heapify, heappop, heappush


t = int(input())

for _ in range(t):
    n = int(input())
    ladder = list(map(int, input().split()))
    heap = [ladder[0]]
    heapify(heap)
    res = 0
    for i in range(1, n):
        removed = []
        elem = 0

        while elem < ladder[i] and len(heap) > 0:
            elem = heappop(heap)
            removed.append(elem)
            res += elem
            