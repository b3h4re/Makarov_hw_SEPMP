def get_children(x):
    return 2*x + 1, 2*x + 2


def dfs(tree, start, path):
    path.append(start)
    for node in get_children(start):
        if node < len(tree) and tree[node] is not None:
            dfs(tree, node, path)


def get_linked_list(tree, res, path):
    if len(tree) == 0:
        return
    if len(tree) == 1:
        res.append(tree[0])
        return
    for node in path:
        res.append(tree[node])
        res.append(None)
    res.pop()


root = [None if x == 'null' else int(x) for x in open("inputs/3.txt", "r").readline().split()]
path = []
dfs(root, 0, path)
linked_list = []
get_linked_list(root, linked_list, path)
print(linked_list)