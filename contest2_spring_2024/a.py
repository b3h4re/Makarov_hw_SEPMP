from heapq import heappush, heappop


class Inf:
    def __init__(self, negative=False):
        self._negative = negative

    def __lt__(self, other):
        return self._negative

    def __le__(self, other):
        return self._negative

    def __ge__(self, other):
        return not self._negative

    def __gt__(self, other):
        return not self._negative

    def __str__(self):
        return ('-' if self._negative else '') + 'INF'

    def __eq__(self, other):
        if other is Inf:
            return True
        return False


def find_cycle(graph, start, heap):
    visited = set()
    color = [0] * n
    dist = [INF for _ in range(n)]
    dist[start] = 0
    heappush(heap, start)
    while len(heap) > 0:
        node = heappop(heap)



INF = Inf()


n, m = map(int, input().split())
g = [set() for _ in range(n)]

for _ in range(m):
    x, y, t = map(int, input().split())
    g[x].add((y, t))

for start in range(n):
    if find_cycle(g, start, []):
        print("yes")
        break
else:
    print("no")