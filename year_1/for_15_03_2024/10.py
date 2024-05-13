from collections import deque


def get_neighbors(x, y, table, visited):
    modifiers = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []
    for dx, dy in modifiers:
        if 0 <= x + dx < len(table) and 0 <= y + dy < len(table[x + dx]) and (x + dx, y + dy) not in visited:
            neighbors.append((x + dx, y + dy))
    return neighbors


def bfs(table, x_s, y_s, visited):
    if table[x_s][y_s] == 1:
        return 0
    q = deque()
    q.append((x_s, y_s, 0))
    visited.add((x_s, y_s))
    while len(q) > 0:
        x, y, dist = q.popleft()
        for x_new, y_new in get_neighbors(x, y, table, visited):
            if table[x_new][y_new] == 1:
                return dist + 1
            q.append((x_new, y_new, dist + 1))


f = open("inputs/10.txt", "r")
n, m = map(int, f.readline().split())
table = [list(map(int, f.readline().split())) for _ in range(n)]
f.close()

new_table = [[0 for _ in range(m)] for __ in range(n)]
for i in range(n):
    for j in range(m):
        new_table[i][j] = bfs(table, i, j, set())
for line in new_table:
    print(*line)