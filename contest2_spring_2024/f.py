def process_test(num_rows, num_cols, cuts, num_cuts):
    if num_cuts < min(num_cols, num_rows):
        return min(num_cols, num_rows)
    cuts = list(map(int, cuts.split()))
    rows_uncut = [set(range(num_cols)) for _ in range(num_rows)]
    for i in range(num_cuts):
        x, y = cuts[2 * i], cuts[2 * i + 1]
        rows_uncut[x].discard(y)
    used_cols = [False] * num_cols
    flow = 0
    for row in range(len(rows_uncut)):
        for col in rows_uncut[row]:
            if not used_cols[col]:
                flow += 1
                used_cols[col] = True
    return flow


if __name__ == "__main__":
    t = int(input())
    ans = []
    for test in range(1, t+1):
        rows, cols, cut = map(int, input().split())
        xy = input()
        ans.append(process_test(rows, cols, xy, cut))
    for elem in ans:
        print(elem)