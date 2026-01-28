import os
import numpy as np
import heapq # Thư viện Python hỗ trợ push, pop, pushpop để xây dựng heap trên 1 mảng

base = os.path.dirname(os.path.abspath(__file__))
MAZE = os.path.join(base, "maze.inp")

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

# Xây dựng MinHeap
class MinHeap(object):
    def __init__(self):                         # Khởi tạo MinHeap rỗng
        self.items = []
        pass
    
    def empty(self):                            # Kiểm tra heap rỗng
        return len(self.items)==0
  
    def push(self, item):                       # Đưa một item vào MinHeap
        heapq.heappush(self.items, item)
        pass
  
    def pop(self):                              # Lấy 1 item có giá trị nhỏ nhất ra khỏi MinHeap
        item = heapq.heappop(self.items)
        return item
    
    def check(self, item):                      # Kiểm tra item có nằm trong MinHeap
        return item in self.items
    
    def update(self, item, new_item):           # Cập nhật lại new_item từ item cho trước
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = new_item
                heapq.heapify(self.items)
        pass
    pass # MinHeap

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

def find_path_UCS(maze, wall_list, start_row, start_col, goal_row, goal_col):
    wall_set = set(wall_list)
    m = len(maze)
    n = len(maze[0])
    if (start_row < 1 or start_row > m or start_col < 1 or start_col > n or goal_row < 1 or goal_row > m or goal_col < 1 or goal_col > n):
        return None
    
    actions = [[1,0],[-1,0],[0,1],[0,-1]]
    parent = {}
    p_closed = []
    g = {}
    open_heap = MinHeap() ## min - heap lưu số bước nhỏ nhất đến goal

    start_point = (start_row,start_col)
    parent[start_point] = None
    open_heap.push((0,start_point))
    g[start_point] = 0

    while open_heap.empty() == False:
        cost, (i, j ) = open_heap.pop()
        if (i, j) == (goal_row,goal_col):
            
            break
        if (i, j) in p_closed:
            continue
        p_closed.append((i,j))
        for dx, dy in actions:
            x, y = i + dx, j + dy
            if 0 < x <= m and 0 < y <= n:
                if Wall(i, j, x, y) not in wall_set:
                    next_cost = g[(i,j)] + 1
                    if (x,y) not in g or next_cost < g[(x,y)]:
                        g[(x,y)] = next_cost
                        parent[(x,y)] = (i,j)
                        open_heap.push((next_cost,(x,y)))
    return parent


def find_path_AStar(maze, wall_list, start_row, start_col, goal_row, goal_col):
    wall_set = set(wall_list) ## đưa về set để tránh trùng lặp
    m = len(maze)
    n = len(maze[0])
    if (start_row < 1 or start_row > m or start_col < 1 or start_col > n or goal_row < 1 or goal_row > m or goal_col < 1 or goal_col > n):
        return None
    
    actions = [[1,0],[-1,0],[0,1],[0,-1]] ## các hướng đi
    parent = {}  ## lưu đỉnh kế trước 
    g = {}
    f = {}
    p_closed = []
    open_heap = MinHeap()

    start_point = (start_row,start_col)
    parent[start_point] = None
    g[start_point] = 0
    f[start_point] = g[start_point] + abs(start_row-goal_row)+abs(start_col-goal_col)
    open_heap.push((f[start_point],start_point))
    ## dùng khoảng cách manhattan cho h(n)

    while open_heap.empty() == False:
        _, (i, j) = open_heap.pop()
        if (i, j) == (goal_row,goal_col):
            break
        if (i, j) in p_closed:
            continue
        p_closed.append((i,j))
        for dx, dy in actions:
            x, y = i + dx, j + dy
            if 0 < x <= m and 0 < y <= n:  ## giới hạn miền biên
                if Wall(i, j, x, y) not in wall_set: ## kiểm tra tại cặp đó có tường ko
                    next_cost = g[(i,j)] + 1
                    if (x,y) not in g or next_cost < g[(x,y)]:
                        g[(x,y)] = next_cost
                        f[(x,y)] = g[(x,y)] + abs(x-goal_row)+abs(y-goal_col)
                        parent[(x,y)] = (i,j)
                        open_heap.push((f[(x,y)],(x,y)))
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