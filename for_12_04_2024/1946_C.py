from collections import deque


def add_connection(graph, start, end):
    graph[start].add(end)
    graph[end].add(start)


def say_no_to_recursion(graph, start, last, x):
    q = deque()
    q.append((start, last))
    stack = []

    while len(q) > 0:
        vertex, parent = q.popleft()

        for neighbor in graph[vertex]:
            if neighbor != parent:
                stack.append((neighbor, vertex))
                q.append((neighbor, vertex))

    res = 1
    subtree = [1] * n
    while len(stack) > 0:
        vertex, parent = stack.pop()
        if subtree[vertex] >= x:
            subtree[vertex] = 0
            res += 1

        subtree[parent] += subtree[vertex]

    return subtree[start], res


def is_cuttable(graph, x, k):
    start = 0
    while len(graph[start]) != 1:
        start += 1
    tmp, components = say_no_to_recursion(graph, start, start, x)
    if components > k + 1:
        return True
    if components == k + 1:
        return tmp >= x
    return False


def get_ans(graph, k):
    l, r = 1, len(graph) + 1
    while l + 1 != r:
        m = (l + r) // 2
        if is_cuttable(g, m, k):
            l = m
        else:
            r = m
    return l


if __name__ == '__main__':
    t = int(input())

    for test in range(1, t+1):
        n, k = map(int, input().split())
        g = [set() for __ in range(n)]
        for __ in range(n-1):
            u, v = map(int, input().split())
            add_connection(g, u-1, v-1)

        print(get_ans(g, k))