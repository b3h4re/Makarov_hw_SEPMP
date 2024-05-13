from collections import deque
from graph import Graph


def path(graph, start, dist):
    q = deque()
    q.append(start)
    dist[start] = 0
    while len(q) > 0:
        vertex = q.popleft()
        for neighbor in graph[vertex]:
            if dist[neighbor] is None:
                dist[neighbor] = dist[vertex] + 1
                q.append(neighbor)


f = open("inputs/6.txt", "r")
n, m = map(int, f.readline().split())
g = Graph(n, oriented=False, weighed=False)
for _ in range(m):
    start, end = map(int, f.readline().split())
    g.add_connection(start, end)
f.close()

dist = [None] * n
path(g, 0, dist)
print(*dist, sep="\n")