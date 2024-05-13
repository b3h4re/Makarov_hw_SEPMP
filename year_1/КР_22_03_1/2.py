from collections import deque


def bfs(graph, start, visited):
    if graph[start][1] > graph[start][2]:
        return
    q = deque()
    q.append(start)
    visited.add(start)
    while len(q) > 0:
        vertex = q.popleft()
        for neighbor in graph[vertex][0]:
            if graph[neighbor][1] == graph[neighbor][2]:
                q.append(neighbor)
                visited.add(neighbor)
            else:
                graph[neighbor][2] += 1


def ans(courses, graph):
    visited = set()
    if courses[0][1] > 0:
        return 'false'
    for start in range(len(courses)):
        if start not in visited:
            bfs(graph, start, visited)
    if len(visited) < len(courses):
        return 'false'
    return 'true'


f = open("inputs/2.txt", "r")
num_courses = int(f.readline())
prerequisites = list(map(int, f.readline().split()))
f.close()

graph = [[set(), 0, 0] for _ in range(num_courses)] # 0 - children; 1 - number of parents; 2 - number of visited parents
courses = [[i, 0] for i in range(num_courses)]
for i in range(0, len(prerequisites)//2 + 1, 2):
    course, requisite = prerequisites[i], prerequisites[i+1]
    graph[requisite][0].add(course)
    graph[course][1] += 1
    courses[course][1] += 1
f.close()

courses.sort(key=(lambda x: x[1]))
print(ans(courses, graph))