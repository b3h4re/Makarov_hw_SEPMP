from collections import deque


def bfs(start, end, parent, used, flows, connections):
    q = deque()
    q.append(start)
    used[start] = True
    while len(q) > 0:
        vertex = q.popleft()
        if vertex == end:
            return
        for neighbor in connections[vertex]:
            if not used[neighbor] and flows[vertex][neighbor] > 0:
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


def adjust_flows(end, flow, flows, parent, connections):
    if parent[end] == -1:
        return
    adjust_flows(parent[end], flow, flows, parent, connections)
    flows[parent[end]][end] -= flow
    flows[end][parent[end]] += flow
    if flows[parent[end]][end] <= 0:
        connections[parent[end]].discard(end)
    if flows[end][parent[end]] > 0:
        connections[end].add(parent[end])


def find_flow(flows, start, end, connections):
    res = 0
    # flows = [[graph[j][i] for i in range(len(graph))] for j in range(len(graph))]

    while True:
        used = [False] * len(flows)
        parent = [-1] * len(flows)
        bfs(start, end, parent, used, flows, connections)

        flow = get_flow(end, parent, flows)
        adjust_flows(end, flow, flows, parent, connections)

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
    connections = [set() for _ in range(n)]

    for i in range(1, num_rows+1):
        graph[0][i], graph[i][0] = 1, 1
        connections[0].add(i)
        connections[i].add(0)
    for i in range(num_cols):
        graph[-1][1+num_rows+i], graph[1+num_rows+i][-1] = 1, 1
        connections[len(graph) - 1].add(1+num_rows+i)
        connections[1+num_rows+i].add(len(graph) - 1)
    for row in range(num_rows):
        for col in range(num_cols):
            graph[1+row][1+num_rows+col] = 1
            connections[1 + row].add(1 + num_rows + col)
    for i in range(num_cuts):
        row, col = cuts[2 * i], cuts[2 * i + 1]
        graph[1 + row][1 + num_rows + col] = 0
        connections[1 + row].discard(1 + num_rows + col)

    return find_flow(graph, 0, n - 1, connections)


if __name__ == "__main__":
    t = int(input())
    ans = []
    for test in range(1, t+1):
        rows, cols, cut = map(int, input().split())
        xy = input()
        ans.append(process_test(rows, cols, xy, cut))
    for elem in ans:
        print(elem)