def calc_levels(levels):
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


def get_parent(x):
    if x % 2 == 1:
        return (x - 1) // 2
    else:
        return (x - 2) // 2


def max_path_from_two_nodes(node1, node2, predicate, levels, root):
    if root[node1] is None or root[node2] is None:
        return 0
    if node1 == node2:
        return root[node1]
    if levels[node2] < levels[node1]:
        node1, node2 = node2, node1
    node2_ = get_parent(node2)
    if levels[node1] != levels[node2]:
        while levels[node2_] > levels[node1]:
            node2_ = get_parent(node2_)

        if node2_ == node1:
            return predicate[node2] + predicate[node1]
    else:
        node2_ = node2
    parent1 = get_parent(node1)
    parent2 = get_parent(node2_)
    while parent2 != parent1:
        parent2 = get_parent(parent2)
        parent1 = get_parent(parent1)
    return predicate[node1] + predicate[node2] - 2*predicate[parent1] + root[parent1]


root = [None if x == "null" else int(x) for x in open("inputs/1.txt", "r").readline().split()]

levels = [0] * len(root)
calc_levels(levels)

predicate = [0] * len(root)
predicate += [0]
predicate[0] = root[0]
for i in range(1, len(root)):
    if root[i] is None:
        continue
    predicate[i] = predicate[get_parent(i)] + root[i]

max_path = 0
for i in range(len(root)):
    for j in range(len(root)):
        max_path = max(max_path, max_path_from_two_nodes(i, j, predicate, levels, root))
print(max_path)