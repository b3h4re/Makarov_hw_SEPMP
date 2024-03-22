root = [None if x == "null" else int(x) for x in open("inputs/1.txt", "r").readline().split()]
print(root)

levels = [0] * len(root)
for level in range(1, len(root)):
    node_left = 2 ** level - 1
    node_right = 2 ** (level + 1) - 1
    for i in range(node_left, node_right):
        if i >= len(root):
            break
        levels[i] = level
    else:
        continue
    break
print(levels)

pred = [0] * len(root)
pred[0] = root[0]
for i in range(1, len(root)):
    if root[i] is None:
        continue
