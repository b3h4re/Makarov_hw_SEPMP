from collections import deque


def bfs(graph, start='JFK'):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    path = [start]
    while len(q) > 0:
        vertex = q.popleft()


inp = open("inputs/4.txt", "r").readline().split()
airports = set(inp)
d = {}
count = 0
for i in airports:
    d.update({i: count})
    count += 1
print(d)
graph = [set() for _ in range(len(airports))]

for i in range(0, len(inp)//2 + 1, 2):
    start, end = inp[i], inp[i+1]
    graph[d[start]].add(end)

bfs(graph)