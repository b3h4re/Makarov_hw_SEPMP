def f(i):
    return i & (i + 1)


def add_to_tree(tree, elem):
    i = elem
    while i < SIZE:
        tree[i] += elem
        i = i | (i + 1)


def summ(tree, i):
    res = 0
    while i >= 0:
        res += tree[i]
        i = (i & (i + 1)) - 1
    return res


t = int(input())

SIZE = int(1e6) + 1

for test in range(1, t+1):
    n = int(input())
    ladder = list(map(int, input().split()))
    tree = [0] * SIZE
    ans = 0
    for i in range(n):
        add_to_tree(tree, ladder[i])
        ans += summ(tree, ladder[i]-1)
    print(ans)