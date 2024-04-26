def ford_bellman(l, e, start, n):
    dist = [1] * n
    parents = [-1] * n
    dist[start] = 0
    for i in range(1, n):
        for u, v in e:
            if dist[v] > dist[u] + l[u][v]:
                dist[v] = dist[u] + l[u][v]
                parents[v] = u
    for u, v in e:
        if dist[v] > dist[u] + l[u][v]:
            return True
    return False


n, m = map(int, input().split())
lengths = [[None for _ in range(n)] for __ in range(n)]
edges = set()

for _ in range(m):
    x, y, t = map(int, input().split())
    lengths[x][y] = t
    edges.add((x, y))


if ford_bellman(lengths, edges, 0, n):
    print('yes')
else:
    print('no')