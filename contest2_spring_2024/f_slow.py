from collections import deque


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


def find_flow(graph, start, end):
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


def process_test(num_rows, num_cols, cuts, num_cuts):
    if num_cuts < min(num_cols, num_rows):
        return min(num_cols, num_rows)
    cuts = list(map(int, cuts.split()))
    n = 2 + num_rows + num_cols
    graph = [[0 for __ in range(n)] for _ in range(n)]

    for i in range(1, num_rows+1):
        graph[0][i], graph[i][0] = 1, 1
    for i in range(num_cols):
        graph[-1][1+num_rows+i], graph[1+num_rows+i][-1] = 1, 1
    for row in range(num_rows):
        for col in range(num_cols):
            graph[1+row][1+num_rows+col] = 1
    for i in range(num_cuts):
        row, col = cuts[2 * i], cuts[2 * i + 1]
        graph[1 + row][1 + num_rows + col] = 0

    return find_flow(graph, 0, n - 1)


if __name__ == "__main__":
    t = int(input())
    ans = []
    for test in range(1, t+1):
        rows, cols, cut = map(int, input().split())
        xy = input()
        ans.append(process_test(rows, cols, xy, cut))
    for elem in ans:
        print(elem)