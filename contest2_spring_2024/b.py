class Inf:
    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True


def dijkstra(graph, lengths, start, end):
    dist = [INF] * len(graph)
    used = [False] * len(graph)
    dist[start] = 0
    for i in range(len(graph)):
        v = None
        for j in range(len(graph)):
            if not used[j] and (v is None or dist[j] < dist[v]):
                v = j
        if dist[v] == INF:
            break
        used[v] = True
        for e in graph[v]:
            if dist[v] + lengths[v][e] < dist[e]:
                dist[e] = dist[v] + lengths[v][e]
    for target in end:
        yield dist[target]


INF = Inf()


n, A, B, C, price = ((lambda x: [int(x[i]) if i < len(x) - 1 else float(x[i]) for i in range(len(x))])
                         (input().split()))
A, B, C = A-1, B-1, C-1
m = int(input())
l = [[None for _ in range(n)] for __ in range(n)]
g = [set() for _ in range(n)]
for _ in range(m):
    s, e, d = (lambda x: [int(x[i])-1 if i < len(x) - 1 else float(x[i]) for i in range(len(x))])(input().split())
    l[s][e], l[e][s] = d, d
    g[s].add(e)
    g[e].add(s)

AB, AC = dijkstra(g, l, A, [B, C])
BC = list(dijkstra(g, l, B, [C]))[0]
if AB == INF or BC == INF:
    print(-1)
else:
    print(price*(AB + BC - AC))