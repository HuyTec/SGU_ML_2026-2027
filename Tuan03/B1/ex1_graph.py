import os

def make_input(G, file_path, verbose = True):
    file_dir = os.path.dirname(file_path)
    if file_dir != "" and not os.path.exists(file_dir):
        os.makedirs(file_dir)
        if verbose: print(f"+ Tạo thư mục: {file_dir}")

    with open(file_path, "wt") as file:
        file.write(f"{len(G)}\n")
        for u in G:
            file.write(f"{u} ")
            for v in G[u]:
                file.write(f"{v} ")
            file.write(f"\n")

        if verbose: print(f"Ghi đồ thị xuống tập tin: {file_path}")
    pass

def load_data(file_path):
    result = None
    if os.path.exists(file_path) == False:
        print("File không tồn tại!")
        result = None
    else:
        G = {}
        with open(file_path, "rt") as file: ## read mode
            n = int(file.readline())
            for line in file: 
                row = line.split()                  ## chia dòng thành các phần tử
                if not row: continue                ## bỏ dòng trống
                u, *next_u  = row                   ## UNPACKING lấy u là phần tử đầu, next_u là các phần tử còn lại  
                G[u] = set(next_u)                  ## đưa về set để tránh lặp đỉnh
            # ...  
            pass
        result = G
        print(f"Load dữ liệu từ {file_path} thành công!")
    return result

def find_path_dfs(G, start, goal):
    if G.get(start) is None or G.get(goal) is None:
        return None

    result = []
    path = {}
    stack = []
    visited = set()

    stack.append(start)
    path[start] = None

    while stack:
        u = stack.pop()     # LIFO → DFS
        visited.add(u)

        if u == goal:
            break

        for v in sorted(G[u], reverse=True):
            if v not in stack and v not in visited:
                path[v] = u
                stack.append(v)

    if goal not in path:
        return []

    cur = goal
    while cur is not None:
        result.append(cur)
        cur = path[cur]

    result.reverse()
    return result


def find_path_bfs(G, start, goal):
    if G.get(start) is None or G.get(goal) is None:
        return None

    result = []
    path = {}
    queue = []
    visited = set()

    queue.append(start)
    path[start] = None

    while queue:
        u = queue.pop(0)     # FIFO → BFS
        visited.add(u)

        if u == goal:
            break

        for v in sorted(G[u]):
            if v not in visited and v not in queue:
                path[v] = u
                queue.append(v)

    if goal not in path:
        return []

    cur = goal
    while cur is not None:
        result.append(cur)
        cur = path[cur]

    result.reverse()
    return result

def deg_calc(G):
    return {u: len(G[u]) for u in G}

def max_deg(G):
    deg = deg_calc(G)
    temp = []
    max_val = max(deg.values())
    for v in G:
        if deg[v]== max_val:
            temp.append(v)
    return temp

def tester():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "dske_ex1.txt")
    G = load_data(file_path)
    print("DEBUG G =", G)
    print(f'Đường đi từ A đến D theo DFS')
    result = find_path_dfs(G, "A", "D")
    print(result)

    print(f'Đường đi từ A đến D theo BFS')
    result2 = find_path_bfs(G, "A", "D")
    print(result2)


if __name__ == "__main__":
    tester()
    





        