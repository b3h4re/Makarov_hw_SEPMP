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

    def remove_connection(self, start, end):
        self._core[start].discard(end)
        if not self._oriented:
            self._core[end].remove(start)

    def __getitem__(self, item):
        return self._core[item]


def find_start(graph):
    for i in range(len(graph)):
        if len(graph[i]) == 1:
            return i


def dfs(graph, start, subtree, last, x, component):
    if subtree > x:
        subtree = 1
        component[0] += 1

    for vertex in graph[start]:
        if vertex != last:
            dfs(graph, vertex, subtree+1, start, x, component)


def is_cuttable(graph, x, k):
    components = [1]
    dfs(graph, find_start(graph), 1, -1, x, components)
    return components[0] > k


def get_ans(graph, k):
    l, r = 1, len(graph) + 1
    while l + 1 != r:
        m = (l + r) // 2
        if is_cuttable(graph, m, k):
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
        g.add_connection(u-1, v-1)
    if _ == 2:
        pass
    print(get_ans(g, k))