from collections import deque


def add_connection(graph, start, end):
    graph[start].add(end)
    graph[end].add(start)


def bfs(graph, start, coloring):
    q = deque()
    colored = set()
    q.append((start, 0, start))
    coloring.append((start, 1))

    max_dist = -1
    while len(q) > 0:
        vertex, dist, parent = q.popleft()


        for neighbor in graph[vertex]:
            if neighbor != parent:
                if dist + 1 >= min_dist:
                    return min_dist + 1
                q.append((neighbor, dist+1, vertex))
    return max_dist


def get_ans(graph):
    if len(graph) == 1:
        print("1\n1 0")
        return
    vertices = [(i, len(graph[i])) for i in range(len(graph))]
    vertices.sort(key=(lambda x: x[1]), reverse=True)
    start = vertices[0][0]
    coloring = []
    bfs(graph, start, coloring)



if __name__ == '__main__':
    t = int(input())

    for test in range(1, t+1):
        n = int(input())

        g = [set() for __ in range(n)]
        for __ in range(n-1):
            u, v = map(int, input().split())
            add_connection(g, u-1, v-1)

        get_ans(g)