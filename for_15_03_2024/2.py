from graph import Graph
from collections import deque


def find_paths(graph, path_exists):
    for start in range(len(graph)):
        q = deque()
        q.append(start)
        path_exists[start].add(start)
        while len(q) > 0:
            vertex = q.popleft()
            for neighbor in graph[vertex][0]:
                if neighbor not in path_exists[start]:
                    path_exists[start].add(neighbor)
                    q.append(neighbor)


f = open("inputs/2.txt")
n, m = map(int, f.readline().split())
g = Graph(n, oriented=True, weighed=True)
for _ in range(m):
    start, end, weight = map(int, f.readline().split())
    g.add_connection(start, end, weight)
f.close()

path_exists = [set() for _ in range(n)]
find_paths(g, path_exists)

components = []
included_vertices = [False] * n
for v in range(n):
    component = set()
    included_vertices[v] = True
    component.add(v)
    for connected in path_exists[v]:
        if v in path_exists[connected]:
            component.add(connected)