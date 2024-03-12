from graph import Graph
from collections import deque


def is_connected(start, graph):
    q = deque()
    q.append(start)
    marked = [False] * len(graph)
    marked[start] = True
    while len(q) > 0:
        vertex = q.popleft()
        for neighbor in graph[vertex]:
            if not marked[neighbor]:
                q.append(neighbor)
                marked[neighbor] = True
    return all(marked)


f = open("inputs/1.txt", "r")
n = int(f.readline())
g = Graph(n, False, False)
m = int(f.readline())
for _ in range(m):
    start, end = map(int, f.readline().split())
    g.add_connection(start, end)
f.close()

if is_connected(0, g):
    print("YES")
else:
    print("NO")