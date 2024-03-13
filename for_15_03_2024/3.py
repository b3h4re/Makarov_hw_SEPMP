from graph import Graph


def dfs(graph, start, visited, path):
    visited.add(start)
    for vertex in graph[start]:
        if vertex not in visited:
            tmp = dfs(graph, vertex, visited, path + str(vertex) + " ")
            if tmp is not None:
                return tmp
        else:
            return path + str(vertex)


f = open("inputs/3.txt")
n, m = map(int, f.readline().split())
g = Graph(n, oriented=True, weighed=False)
for _ in range(m):
    start, end = map(int, f.readline().split())
    g.add_connection(start, end)
f.close()

visited = set()
for start in range(n):
    visited = set()
    ans = dfs(g, start, visited, "")
    if ans is not None:
        print(ans)
        break
else:
    print("YES")
