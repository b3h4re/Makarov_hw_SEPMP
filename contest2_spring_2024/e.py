from collections import deque


# def dfs(graph, flows, used, start, end, flow, num):
#     if start == end:
#         return flow
#     used[start] = num
#     for vertex, edge in graph[start]:
#         if used[vertex] != num and edge - flows[start][vertex] > 0:
#             delta = dfs(graph, flows, used, vertex, end, min(flow, edge - flows[start][vertex]), num)
#             if delta > 0:
#                 flows[start][vertex] += delta
#                 flows[vertex][start] -= delta
#                 return delta
#     return 0


def bfs(graph, start, end, parent, used, flows):
    q = deque()
    q.append(start)
    used[start] = True
    while len(q) > 0:
        vertex = q.popleft()
        if vertex == end:
            return
        for neighbor in range(len(graph)):
            if flows[vertex][neighbor] > 0 and not used[neighbor]:
                used[neighbor] = True
                parent[neighbor] = vertex
                q.append(neighbor)


def get_flow(end, parent, flows):
    if parent[end] == -1:
        return
    flow = get_flow(parent[end], parent, flows)
    if flow is None:
        return flows[parent[end]][end]
    return min(flows[parent[end]][end], get_flow(parent[end], parent, flows))


def adjust_flows(end, flow, flows, parent):
    if parent[end] == -1:
        return
    adjust_flows(parent[end], flow, flows, parent)
    flows[parent[end]][end] -= flow
    flows[end][parent[end]] += flow


def find_flow(graph, start,  end):
    res = 0
    flows = [[graph[j][i] for i in range(len(graph))] for j in range(len(graph))]
    while True:
        used = [False] * len(graph)
        parent = [-1] * len(graph)
        bfs(graph, start, end, parent, used, flows)

        flow = get_flow(end, parent, flows)
        adjust_flows(end, flow, flows, parent)

        if flow is None:
            break
        res += flow
    return res


def process_test(graph):
    mn = None
    for v in range(1, len(graph)):
        flow = find_flow(graph, 0, v)
        if mn is None:
            mn = flow
        mn = min(mn, flow)
    return mn


if __name__ == "__main__":
    t = int(input())
    ans = []
    for test in range(1, t+1):
        n = int(input())

        cities = [[0 for __ in range(n)] for _ in range(n)]
        for i in range(n):
            line = list(map(int, input()))
            for j in range(n):
                if line[j] > 0:
                    cities[i][j] = line[j]
        ans.append(process_test(cities))

    for elem in ans:
        print(elem)
