from graph import Graph


t = int(input())

for _ in range(t):
    n = int(input())
    g = Graph(n=n, oriented=False, weighed=False)
    for __ in range(n-1):
        u, v = map(int, input().split())
        g.add_connection(u, v)
    