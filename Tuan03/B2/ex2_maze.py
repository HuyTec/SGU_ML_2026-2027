import os
import numpy as np

MAZE = "maze.inp"

class Wall:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.a = (x1,y1)
        self.b = (x2,y2)
        pass
    def __eq__(self, other):
        return {self.a, self.b} == {other.a, other.b}
    def __repr__(self):
        return f"({self.a},{self.b})"
    def __hash__(self):
        return hash(frozenset([self.a,self.b]))
        pass
    pass

def readfile(debug = None):
    wall_list = []
    with open(MAZE, "rt") as file:
        content = file.readlines()

    m = int(content[0].strip())
    n = int(content[1].strip())

    maze = np.zeros((m,n), dtype=int)
    data = np.array([list(map(int, row.split())) for row in content[2:]])

    for d in data:
        x1, y1, x2, y2 = d
        wall_list.append(Wall(x1, y1, x2, y2))

    print("Ma trận : ")
    print(maze)
    print("Danh sách vị trí các tường")
    print(wall_list)
    
    if debug is not None: debug.update(locals())
    return wall_list, maze

def find_path_BFS(maze, wall_list, start_row, start_col, goal_row, goal_col):
    wall_set = set(wall_list)
    m = len(maze)
    n = len(maze[0])
    if (start_row < 1 or start_row > m or start_col < 1 or start_col > n or goal_row < 1 or goal_row > m or goal_col < 1 or goal_col > n):
        return None
    
    actions = [[1,0],[-1,0],[0,1],[0,-1]]
    visited = set()
    parent = {}
    p_open = []
    p_closed = []

    start_point = (start_row,start_col)
    parent[start_point] = None
    p_open.append(start_point)
    visited.add(start_point)

    while len(p_open)>0:
        i, j = p_open.pop(0)
        if (i, j) == (goal_row,goal_col):
            break
        p_closed.append((i,j))
        for dx, dy in actions:
            x, y = i + dx, j + dy
            if 0 < x <= m and 0 < y <= n:
                if (x,y) not in visited:
                    if Wall(i, j, x, y) not in wall_set:
                        visited.add((x,y))
                        parent[(x,y)] = (i,j)
                        p_open.append((x,y))
    return parent

def find_path_DFS(maze, wall_list, start_row, start_col, goal_row, goal_col):
    wall_set = set(wall_list) ## đưa về set để tránh trùng lặp
    m = len(maze)
    n = len(maze[0])
    if (start_row < 1 or start_row > m or start_col < 1 or start_col > n or goal_row < 1 or goal_row > m or goal_col < 1 or goal_row > n):
        return None
    
    actions = [[1,0],[-1,0],[0,1],[0,-1]] ## các hướng đi
    visited = set() ## tập hợp đánh dấu ô đã thăm
    parent = {}  ## lưu đỉnh kế trước 
    p_open = []  ## tập để mở rộng
    p_closed = []

    start_point = (start_row,start_col)
    parent[start_point] = None
    p_open.append(start_point)
    visited.add(start_point)

    while len(p_open)>0:
        i, j = p_open.pop()
        if (i, j) == (goal_row,goal_col):
            break
        p_closed.append((i,j))
        for dx, dy in actions:
            x, y = i + dx, j + dy
            if 0 < x <= m and 0 < y <= n:  ## giới hạn miền biên
                if (x,y) not in visited:
                    if Wall(i, j, x, y) not in wall_set: ## kiểm tra tại cặp đó có tường ko
                        visited.add((x,y))
                        parent[(x,y)] = (i,j)
                        p_open.append((x,y))
    return parent

def path(parent, start_row, start_col, goal_row, goal_col):
    result = []
    goal = (goal_row,goal_col)
    while goal is not None:
        result.append(goal)
        goal = parent[goal]

    return result


if __name__ == "__main__":
    readfile(debug=globals())