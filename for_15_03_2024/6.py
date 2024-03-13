from collections import deque

from graph import Graph


def bfs(graph, start, dist):
    q = deque()
    q.append(start)
    visited = {start}
    dist[start] = 0
    while len(q) > 0:
        vertex = q.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                dist[neighbor] = dist[vertex] + 1


f = open("inputs/6.txt", "r")
n, m = map(int, f.readline().split())
g = Graph(n, oriented=False, weighed=False)
for _ in range(m):
    start, end = map(int, f.readline().split())
    g.add_connection(start, end)
f.close()

dist = [None] * n
bfs(g, 0, dist)
print(*dist, sep='\n')