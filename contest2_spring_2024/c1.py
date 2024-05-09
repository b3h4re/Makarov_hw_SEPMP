def find_mst_kra(graph, out):



def get_ans(num_vertices, graph_edges):
    mst = [set() for _ in range(num_vertices)]
    graph_edges.sort(key=(lambda x: x[-1]))
    find_mst_kra(graph_edges, mst)
    return


if __name__ == "__main__":
    n, m, p = map(int, input().split())
    unsafe = list(map(int, input().split()))
    house_edges = []
    for _ in range(m):
        xi, yi, cost = map(int, input().split())
        house_edges.append((xi, yi, cost))
    print(get_ans(n, house_edges))