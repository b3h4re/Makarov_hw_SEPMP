from collections import deque
from graph import Graph


def bfs(graph, start, dist, max_len):
    res = (max_len, -1, "")
    dist[start] = 0
    q = deque()
    q.append((start, f"{start}"))
    while len(q) > 0:
        vertex, path = q.popleft()
        for neighbor in graph[vertex]:
            if dist[neighbor] is None:
                dist[neighbor] = dist[vertex] + 1
                q.append((neighbor, path + f" {neighbor}"))
            else:
                if dist[vertex] + 1 - dist[neighbor] < res[0]:
                    res = (dist[vertex] + 1 - dist[neighbor], neighbor, path)
    return res


f = open("inputs/8.txt", "r")
n, m = map(int, f.readline().split())
graph = Graph(n, oriented=True, weighed=False)
for _ in range(m):
    start, end = map(int, f.readline().split())
    graph.add_connection(start, end)
f.close()


min_cycle = (n+1, -1)
for start in range(n):
    dist = [None] * n
    cycle = bfs(graph, start, dist, min_cycle[0])
    if cycle[0] < min_cycle[0]:
        min_cycle = cycle
if min_cycle[1] == -1:
    print("NO CYCLES")
else:
    print(min_cycle[2])