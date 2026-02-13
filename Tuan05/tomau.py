import os

base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "tomau.inp")

def readFile(file_path = PATH, debug = True):
    with open(file_path, "rt") as file:
        content = file.readlines()
    n = int(content[0].strip())
    graph = {}
    for i in range (1, len(content)):
        u, v = list(map(int, content[i].split()))
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
        pass

    if debug: print("Đọc dữ liệu thành công!")
    pass
    return n, graph

def tomau_backtracking(n, graph):
    pass



if __name__ == "__main__":
    n, graph = readFile()
    print(n)
    print(graph)