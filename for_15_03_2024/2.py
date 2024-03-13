from graph import Graph
from collections import deque


def find_paths(graph, start, comp):
    q = deque()
    q.append(start)
    comp.add(start)
    while len(q) > 0:
        vertex = q.popleft()
        for neighbor, _ in graph[vertex]:
            if neighbor not in comp:
                comp.add(neighbor)
                q.append(neighbor)


def calculate_total_weight(graph, component):
    res = 0
    added = set()
    visited = set()
    for vertex in component:
        if vertex not in visited:
            visited.add(vertex)
            for neighbor, weight in graph[vertex]:
                if (vertex, neighbor) not in added:
                    added.add((vertex, neighbor))
                    added.add((neighbor, vertex))
                    res += weight
    return res


f = open("inputs/2.txt")
n, m = map(int, f.readline().split())
g = Graph(n, oriented=False, weighed=True)
for _ in range(m):
    start, end, weight = map(int, f.readline().split())
    g.add_connection(start, end, weight)
f.close()

components = []
used = set()
for start in range(n):
    component = set()
    if start not in used:
        find_paths(g, start, component)
        used.update(component)
        components.append(component)

ans = []
for component in components:
    ans.append(calculate_total_weight(g, component))
ans.sort()
print(*ans, sep='\n')