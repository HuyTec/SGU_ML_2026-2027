import os
import heapq

base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "tomau.inp")

format_matrix = 0

def readFile(file_path = PATH, debug = True):
    with open(file_path, "rt") as file:
        content = file.readlines()
    n = int(content[0].strip())
    matrix = [[format_matrix]*n for _ in range(n)]
    for i in range (1, len(content)):
        u, v = list(map(int, content[i].split()))
        matrix[u-1][v-1] = 1
        matrix[v-1][u-1] = 1
        pass

    if debug: print("Đọc dữ liệu thành công!")
    pass
    return n, matrix

def in_matran(matrix):
    for row in matrix:
        for col in row:
            print(f'{col}', end=" ")
        print()
 
def hople(u, c, graph, color): ## phần quan trọng nhất
    for i in range(0, u):
        if (graph[u][i] == 1 and c == color[i]):
            return False
    return True
"""--------------------------------------------------------------------------"""
def tomau_backtracking(n, graph, limit_color = None, all_solution = False):
    result = []
    val = n if limit_color is None else limit_color
    color = [0]*n

    def backtracking(u):
        if u == n: 
            result.append(color.copy())
            return not all_solution
        for c in range(1, val+1):
            if hople(u, c, graph, color):
                color[u] = c
                if backtracking(u+1): return True
                color[u] = 0
        return False
    
    backtracking(0)
    if all_solution: print(len(result))
    return result

"""--------------------------------------------------------------------------"""

def tomau(result):
    if result is None or len(result) == 0:
        print(0)
        return
    kq = result[0]
    maxcolor = max(kq)
    classify = {}
    for i in range(0, len(kq)):
        if kq[i] not in classify:
            classify[kq[i]] = []
        classify[kq[i]].append(i)
    print(maxcolor)
    for c in range (1, maxcolor+1):
        for u in classify[c]:
            print(f'{u+1}', end=" ")
        print()
    pass

"""--------------------------------------------------------------------------"""

def bac(graph, u):
    cnt = 0
    for v in graph[u]:
        if v==1: cnt += 1
        pass
    return cnt
    
def tomau_greedy(n, graph, debug = False):
    result = []
    color = [0]*n

    deg = []
    for i in range(0, n):
        deg.append((bac(graph, i), i))
    deg.sort(reverse=True)
    for _, u in deg:
        if debug: print(f'current_vertice = {u}')
        used = set()
        for v in range(0, n):
            if graph[u][v] == 1:
                if color[v] != 0:
                    used.add(color[v])
        if debug: print(f'used_color = {used}')
        c = 1
        while c in used:
            c += 1
        color[u] = c
        if debug:
            print(f'coloring {u} by {c}')   
            print(f'color = {color}') 
            print()      
    result.append(color)
    return result

"""--------------------------------------------------------------------------"""
def tomau_heuristic(n, graph, debug = False):
    result = []
    color = [0]*n

    dsatur = []
    for i in range(0, n):
        heapq.heappush(dsatur, (0, -bac(graph, i), i))
    if debug: print(dsatur)

    while dsatur:
        s, _, u = heapq.heappop(dsatur)
        
        if color[u] != 0: continue
        if debug: print(dsatur)
        if debug: print(f'current_vertice = {u} with s = {-s}')

        used = set(color[v] for v in range(n) if graph[u][v] ==1 and color[v] != 0)
        if debug: print(f'used_color = {used}')
        c = 1
        while c in used:
            c += 1
        color[u] = c
        if debug:
            print(f'coloring {u} by {c}')   
            print(f'color = {color}') 
            print()      
        for v in range(n):
            if graph[u][v] == 1 and color[v] == 0:
                sat = len(set(color[w] for w in graph[v] if color[w] != 0))
                deg = bac(graph, v)
                heapq.heappush(dsatur, (-sat, -deg, v))

    result.append(color)
    return result

if __name__ == "__main__":
    n, graph = readFile()
    # print(n)
    # in_matran(graph)
    # result = tomau_backtracking(n, graph, all_solution=True, limit_color=3)
    # print(result)
    # tomau(result)
    tomau_heuristic(n, graph, debug=True)
    pass

