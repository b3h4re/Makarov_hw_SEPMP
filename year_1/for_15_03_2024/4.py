from graph import Graph


def dfs(graph, start, stack, visited, visited_this_iteration):
    visited[start] = True
    visited_this_iteration.add(start)
    for vertex in graph[start]:
        if vertex in visited_this_iteration:
            return "CYCLE!"
        if not visited[vertex]:
            tmp = dfs(graph, vertex, stack, visited, visited_this_iteration)
            if tmp is not None:
                return tmp
    stack.append(start)


f = open("inputs/4.txt")
n, m = map(int, f.readline().split())
graph = Graph(n, oriented=True, weighed=False)
for _ in range(m):
    start, end = map(int, f.readline().split())
    graph.add_connection(start, end)
f.close()

visited = [False] * n
stack = []

for start in range(n):
    visited_this_iteration = set()
    if not visited[start]:
        cycle = dfs(graph, start, stack, visited, visited_this_iteration)
        if cycle is not None:
            print("NO")
            break
else:
    print(*list(reversed(stack)))
