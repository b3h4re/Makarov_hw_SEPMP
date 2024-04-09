class Graph:
    def __init__(self, n, oriented=False, weighed=False):
        self._oriented = oriented
        self._weighed = weighed
        self._core = [set() for _ in range(n)]

    def __len__(self):
        return len(self._core)

    def add_connection(self, start, end, weight=0):
        self._core[start].add((end, weight) if self._weighed else end)
        if not self._oriented:
            self._core[end].add((start, weight) if self._weighed else start)

    def __getitem__(self, item):
        return self._core[item]


def dfs(graph, start, visited, subtree):
    visited.add(start)
    for vertex in graph[start]:
        if vertex not in visited:
            dfs(graph, vertex, visited, subtree+1)


def is_cuttable(graph, x, k):
    start = 0
    while len(graph[start]) > 1:
        start += 1
    visited = set()
    while len(visited) < len(graph):
        dfs(graph, start, visited, set())


def get_ans(graph, k):
    l, r = 1, len(graph) + 1
    while l + 1 != r:
        m = (l + r) // 2
        if is_cuttable(graph, m):
            l = m
        else:
            r = m
    return l


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    g = Graph(n=n, oriented=False, weighed=False)
    for __ in range(n-1):
        u, v = map(int, input().split())
        g.add_connection(u, v)
    print(get_ans(g, k))