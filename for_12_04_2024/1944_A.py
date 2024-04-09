def get_ans(bridges, can_destroy):
    if can_destroy == 0:
        return bridges


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    print(get_ans(n, k))