def add_connection(graph, start, end):
    graph[start-1].add(end-1)
    graph[end-1].add(start-1)


def dfs(graph, start, last, color, edges, cycles, ans):
    color[start] = 1
    ok = True
    for vertex in graph[start]:
        if vertex == last:
            continue
        if color[vertex] == 0:
            edges.append((start, vertex))
            dfs(graph, vertex, start, color, edges, cycles,ans)
            edges.pop()
        elif color[vertex] == 1:
            ok = not cycles[start][vertex]
            cycles[start][vertex], cycles[vertex][start] = True, True
            length = 2
            for i in range(len(edges)-1, -1, -1):
                s, e = edges[i]
                if e == vertex:
                    break
                ok *= not cycles[s][e]
                cycles[s][e], cycles[e][s] = True, True
                length += 1
            ans.append(length)
        if not ok:
            return
    color[start] = 2


n, m = map(int, input().split())
g = [set() for _ in range(n)]

for _ in range(m):
    ki, *path = map(int, input().split())
    for i in range(1, ki):
        add_connection(g, path[i-1], path[i])

colors = [0] * n
in_cycle = [[False for _ in range(n)] for __ in range(n)]
edges = []
cycle_lengths = []

dfs(g, 0, -1, colors, edges, in_cycle, cycle_lengths)
for i in range(n):
    if colors[i] != 2:
        print(0)
        break
else:
    ans = 1
    for elem in cycle_lengths:
        ans *= elem
    print(ans)