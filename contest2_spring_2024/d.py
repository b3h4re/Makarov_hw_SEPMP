INF = int(1e12)


def rho2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1])**2


def find_mst(s, posts, dist):
    used = [False] * s
    cur = 0
    used[cur] = True
    dist[cur] = 0
    for i in range(1, s):
        for j in range(s):
            if not used[j] and rho2(posts[cur], posts[j]) < dist[j]:
                dist[j] = rho2(posts[cur], posts[j])

        mn = INF
        for j in range(s):
            if not used[j] and dist[j] < mn:
                mn = dist[j]
                cur = j
        used[cur] = True


def process_test(s, posts, res):
    dist = [INF] * len(posts)
    find_mst(len(posts), posts, dist)
    dist.sort()
    res.append(
        "{:.2f}".format(dist[-s]**0.5)
    )


if __name__ == "__main__":
    n = int(input())
    ans = []
    for test in range(1, n+1):
        satellites, p = map(int, input().split())
        ps = []
        for _ in range(p):
            ps.append(tuple(map(int, input().split())))
        process_test(satellites, ps, ans)
    for elem in ans:
        print(elem)