n = int(input())
not_root = set()
vertices = set()
for _ in range(n):
    start, end = map(int, input().split())
    not_root.add(end)
    vertices.add(start)
    vertices.add(end)
print(len(vertices) - len(not_root))