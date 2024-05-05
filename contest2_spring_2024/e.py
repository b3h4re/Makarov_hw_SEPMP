def dfs(graph, flows, used, start, end, flow, num):
    if start == end:
        return flow
    used[start] = num
    for vertex, edge in graph[start]:
        if used[vertex] != num and edge - flows[start][vertex] > 0:
            delta = dfs(graph, flows, used, vertex, end, min(flow, edge - flows[start][vertex]), num)
            if delta > 0:
                flows[start][vertex] += delta
                flows[vertex][start] -= delta
                return delta
    return 0


def find_flow(graph, start,  end):
    used = [0] * len(graph)
    flows = [[0 for _ in range(len(graph))] for __ in range(len(graph))]
    num = 1
    x, res = 1, 0
    while x > 0:
        x = dfs(graph, flows, used, start, end, int(1e12), num)
        res += x
        num += 1
    return res


def process_test(graph):
    mn = int(1e12)
    for v in range(1, len(graph)):
        flow = find_flow(graph, 0, v)
        mn = min(flow, mn)
    return mn


if __name__ == "__main__":
    t = int(input())
    ans = []
    for test in range(1, t+1):
        n = int(input())

        cities = [set() for _ in range(n)]
        for i in range(n):
            line = list(map(int, input()))
            for j in range(n):
                if line[j] > 0:
                    cities[i].add(
                        (j, line[j])
                    )
        ans.append(process_test(cities))

    for elem in ans:
        print(elem)
