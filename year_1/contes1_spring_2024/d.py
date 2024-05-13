class Graph:
    def __init__(self):
        self._core = {}
        self._names = set()

    def add_connection(self, start, end, relation):
        if relation == '>':
            start, end = end, start
        if start not in self._names:
            self._names.add(start)
            self._core[start] = set()
        if end not in self._names:
            self._names.add(end)
            self._core[end] = set()
        self._core[start].add(end)

    def __getitem__(self, item):
        if item in self._names:
            return self._core[item]
        return set()

    def get_names(self):
        return self._names


def is_correct(graph, color, start):
    color[start] = 1
    is_ok = True
    for vertex in graph[start]:
        if color[vertex] == 1:
            return False
        if color[vertex] == 2:
            continue
        is_ok = is_correct(graph, color, vertex)
    color[start] = 2
    return is_ok


f = open('input.txt')
inp = f.readlines()
f.close()
mod = 1
try:
    n = int(inp[0].strip())
except:
    n = len(inp)
    mod = 0


smurfs = Graph()

for i in range(mod, n+mod):
    start, relation, end = inp[i].split()
    smurfs.add_connection(start, end, relation)

colors = {}
for name in smurfs.get_names():
    colors[name] = 0


for start in smurfs.get_names():
    if not is_correct(smurfs, colors, start):
        answer = 'impossible'
        break
else:
    answer = 'possible'

f = open('output.txt', "w")
f.write(answer)
f.close()