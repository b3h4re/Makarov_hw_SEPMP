from collections import deque
from heapq import heappush, heappop


def rho2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1])**2


def find_components(graph, out):
    used = [False] * len(graph)
    for start in range(1, len(graph)):
        if not used[start]:
            out.append(set())
            q = deque()
            q.append(start)
            while len(q) > 0:
                vertex = q.popleft()
                used[vertex] = True
                out[-1].add(vertex)
                for neighbor in graph[vertex]:
                    if not used[neighbor]:
                        q.append(neighbor)


def get_dist_between_components(coords, c1, c2):
    min_dist = None
    min_v1 = None
    min_v2 = None
    for v1 in c1:
        for v2 in c2:
            r2 = rho2(coords[v1], coords[v2])
            if min_dist is None:
                min_dist = r2
                min_v1, min_v2 = v1, v2
                continue
            if r2 < min_dist:
                min_dist = r2
                min_v1, min_v2 = v1, v2
    return [min_dist, min_v1, min_v2]


INF = int(1e12)


f = open("input.txt", "r")
tests = int(f.readline())

ans = []
for test in range(1, tests+1):
    n = int(f.readline())
    ans.append([])
    city_coordinates = [(None, None)]
    for i in range(n):
        xi, yi = map(int, f.readline().split())
        city_coordinates.append((xi, yi))
    roads = [set() for _ in range(n+1)]
    m = int(f.readline())
    for _ in range(m):
        s, e = map(int, f.readline().split())
        roads[s].add(e)
        roads[e].add(s)

    components = []
    find_components(roads, components)
    if len(components) == 1:
        print('fine')
        print()
        continue
    components.sort(key=len, reverse=True)

    connected = [False] * len(components)
    dists = []
    comp = 0
    connected[comp] = True
    joined = 1
    while joined < len(components):
        for i in range(1, len(components)):
            if not connected[i]:
                heappush(dists,
                         tuple(get_dist_between_components(city_coordinates, components[comp], components[i]) + [i])
                         )
        connection = None
        while connection is None or connected[connection[3]]:
            connection = heappop(dists)
        # print(connection[1], connection[2])
        # output.write(f"{connection[1]} {connection[2]}\n")
        ans[-1].append(
            (min(connection[1], connection[2]), max(connection[1], connection[2]))
        )
        joined += 1
        connected[connection[3]] = True
        comp = connection[3]
    ans[-1].sort()
    # output.write("\n")
f.close()
output = open('output.txt', "w")
for elem in ans:
    for con in elem:
        output.write(f"{con[0]} {con[1]}\n")
    output.write("\n")
output.close()
