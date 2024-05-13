def get_moves_from_position(x, y, table):
    modifiers = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    next_positions = set()
    for d_x, d_y in modifiers:
        if 0 <= x + d_x <= len(table) and 0 <= y + d_y <= len(table[x+d_x]) and table[x+d_x][y+d_y] != "X":
            next_positions.add((x+d_x, y+d_y))
    return next_positions


def search(table, x_s, y_s, x_e, y_e, max_dist, dist, visited):
    visited.add((x_s, y_s))
    if dist >= max_dist:
        return max_dist
    if x_s == x_e and y_s == y_e:
        return dist
    moves = get_moves_from_position(x_s, y_s, table)
    if (x_e, y_e) in moves:
        return dist + 1
    ans = max_dist
    for x, y in moves:
        if (x, y) not in visited:
            ans = min(ans, search(table, x, y, x_e, y_e, max_dist, dist+1, visited))
            max_dist = ans
    return ans


f = open("inputs/7.txt")
n, m = map(int, f.readline().split())
x1, y1 = map(int, f.readline().split())
x2, y2 = map(int, f.readline().split())
table = [f.readline().strip() for _ in range(n)]
f.close()

ans = search(table, x1, y1, x2, y2, n*m, 0, set())

if ans == n*m:
    print("INF")
else:
    print(ans)