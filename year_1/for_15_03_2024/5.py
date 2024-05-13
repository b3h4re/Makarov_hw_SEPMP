from collections import deque

from graph import Graph


def find_paths(graph, start, comp, stolen):
    q = deque()
    q.append(start)
    comp.add(start)
    while len(q) > 0:
        vertex = q.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in comp and neighbor != stolen:
                comp.add(neighbor)
                q.append(neighbor)


def find_components(graph, components, stolen):
    used = set()
    for start in range(len(graph)):
        component = set()
        if start not in used and start != stolen:
            find_paths(graph, start, component, stolen)
            used.update(component)
            components.append(component)
        if len(components) > 1:
            return 2
    return len(components)


f = open("inputs/5.txt")
n, m = map(int, f.readline().split())
g = Graph(n, oriented=False, weighed=False)
for _ in range(m):
    start, end = map(int, f.readline().split())
    g.add_connection(start-1, end-1)
f.close()

groups_start = find_components(g, [], -1)
people_to_steal = []

for person in range(1, n+1):
    groups = find_components(g, [], person-1)
    if groups > groups_start:
        people_to_steal.append(person)
if len(people_to_steal) > 0:
    print(*people_to_steal)
else:
    print(-1)