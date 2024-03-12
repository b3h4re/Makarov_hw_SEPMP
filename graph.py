class Graph:
    def __init__(self, n, oriented=False, weighed=False):
        self._oriented = oriented
        self._weighed = weighed
        self._core = [set() for _ in range(n)]

    def __len__(self):
        return len(self._core)

    def add_connection(self, start, end, weight=0):
        self._core[start].add((end, weight) if self._weighed else end)
        if not self._oriented:
            self._core[end].add((start, weight) if self._weighed else end)

    def __getitem__(self, item):
        return self._core[item]