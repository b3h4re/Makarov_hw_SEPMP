from collections import deque


def get_next_vertices(vertex, stage, rows_uncut, end):
    if stage == 0:
        return range(len(rows_uncut))
    elif stage == 1:
        for i in rows_uncut[vertex]:
            yield i
    elif stage == 2:
        return end


def get_i(vertex, stage, graph):
    if stage == 0:
        return 0
    if stage == 1:
        return vertex + 1
    if stage == 2:
        return 1 + len(graph) + vertex
    return len(graph) - 1


def bfs(graph, start, end, parent, used, flows):
    q = deque()
    q.append((start, 0))
    used[get_i(start, 0, graph)] = True
    while len(q) > 0:
        vertex, stage = q.popleft()
        if vertex == end:
            return
        for neighbor in get_next_vertices(vertex, stage, graph, end):
            if flows[vertex][neighbor] > 0 and not used[get_i(neighbor, stage + 1, graph)]:
                used[get_i(neighbor, stage + 1, graph)] = True
                parent[get_i(neighbor, stage + 1, graph)] = get_i(vertex, stage, graph)
                q.append((neighbor, stage + 1))


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


def find_flow(graph, start, end, num_rows, num_cols):
    res = 0
    # flows = [[graph[j][i] for i in range(len(graph))] for j in range(len(graph))]
    flows = ([num_rows] + [len(graph[i]) for i in range(num_rows)] +
             [1 for _ in range(num_cols)] + []) # TODO flows array properly
    while True:
        used = [False] * (end + 1)
        parent = [-1] * (end + 1)
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
    rows_uncut = [set(range(num_cols)) for _ in range(num_rows)]
    for i in range(num_cuts):
        x, y = cuts[2 * i], cuts[2 * i + 1]
        rows_uncut[y].discard(x)

    return find_flow(rows_uncut, 0, n - 1, num_rows, num_cols)


if __name__ == "__main__":
    t = int(input())
    ans = []
    for test in range(1, t+1):
        rows, cols, cut = map(int, input().split())
        xy = input()
        ans.append(process_test(rows, cols, xy, cut))
    for elem in ans:
        print(elem)
