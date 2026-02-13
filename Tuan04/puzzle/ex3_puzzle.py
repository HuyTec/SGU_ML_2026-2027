## 4 8 1 
## 6 3 0
## 2 7 5

## 1 2 3
## 4 5 6
## 7 8 0

import numpy as np
import os
import time
from collections import deque
import heapq
import itertools as it


base = os.path.dirname(os.path.abspath(__file__))
PUZZLE = os.path.join(base, "puzzle.inp")

actions = [(-1,0),(1,0),(0,-1),(0,1)]

class State:
    
    def __init__(self, state, parent = None):
        self.state = tuple(tuple(row) for row in state)
        self.parent = parent
        pass

    def to_state(self):
        return self.state
    
    def __eq__(self, other): ## So sánh giữa cùng đối tượng
        if not isinstance(other, State): return False
        return self.state == other.state
    
    def __repr__(self):
        return f"[{self.state}]"

    def __hash__(self): ## Cho phép thêm vào set, dict, list như biến thường
        return hash(self.state)
    
    def pos0(self):
        s = self.state
        for i, row in enumerate(s):
            for j, x in enumerate(row):
                if x == 0: return i, j        
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

def readfile(debug=None):
    with open(PUZZLE, "rt") as file:
        content = file.readlines()

    start = tuple(tuple(map(int, line.split())) for line in content[0:3])
    goal = tuple(tuple(map(int, line.split())) for line in content[3:6])

    if debug is not None: print("Đọc file thành công!")

    return State(start), State(goal)


def generator_state(state, dx, dy):
    s = state.state
    n = len(s)
    i, j = state.pos0()

    if (dx, dy) not in actions: return None

    if not (0 <= i+dx < n and 0 <= j+dy < n): return None
    
    a = np.array(s) # parse sang array để swap
    a[i, j], a[i+dx, j+dy] = a[i+dx, j+dy], a[i, j] # swap ô

    after = tuple(tuple(int(x) for x in row) for row in a)
    new_state = State(after)
    new_state.parent = state
    return new_state


def solve_UCS(start, goal):
    if start is None or goal is None: return None
    state_cnt = 0
    open_heap = MinHeap()
    g = {}
    closed = []

    counter = it.count() ## bộ đếm 
    open_heap.push((0, next(counter) ,start))
    g[start] = 0 # giá trị tại ô bắt đầu  tương đương số bước là 0
    while open_heap.empty() == False:
        cost ,_, state = open_heap.pop()

        if state in closed:
            continue

        if state == goal:
            return state, state_cnt
        
        closed.append(state)

        for dx, dy in actions:
            next_state = generator_state(state, dx, dy)
            state_cnt += 1
            if next_state is None: continue
            cost = g[state] + 1
            if next_state not in g or cost < g[next_state]:
                next_state.parent = state
                g[next_state] = cost
                open_heap.push((g[next_state], next(counter) , next_state))
    return None

def heuristic_hamming(state1, goal):
    wrong_pos = 0
    begin = state1.state
    end = goal.state

    for i, row in enumerate(begin):
        for j, x in enumerate(row):
            if x!= 0 and x!= end[i][j]: wrong_pos += 1
    return wrong_pos

def heuristic_manhattan(state1, goal):
    distance = {}
    begin = state1.state
    end = goal.state
    for i in range(len(end)):
        for j in range(len(begin[0])):
            distance[end[i][j]] = (i,j)

    dist = 0
    for i in range(len(begin)):
        for j in range(len(begin[0])):
            x = begin[i][j]
            if x !=0:
                gi, gj = distance[x]
                dist += abs(i - gi)+abs(j - gj)
    return dist
    

def solve_AStar_hamming(start, goal):
    if start is None or goal is None: return None
    state_cnt = 0;
    open_heap = MinHeap()
    g = {}; f = {}
    closed = []

    counter = it.count() ## bộ đếm 
    
    g[start] = 0 # giá trị tại ô bắt đầu  tương đương số bước là 0
    f[start] = g[start] + heuristic_hamming(start,goal)
    open_heap.push((f[start], next(counter) ,start))

    while open_heap.empty() == False:
        cost ,_, state = open_heap.pop()

        if state in closed:
            continue

        if state == goal:
            return state, state_cnt
        
        closed.append(state)

        for dx, dy in actions:
            next_state = generator_state(state, dx, dy)
            state_cnt += 1
            if next_state is None: continue
            cost = g[state] + 1
            if next_state not in g or cost < g[next_state]:
                next_state.parent = state
                g[next_state] = cost
                f[next_state] = g[next_state] + heuristic_hamming(next_state, goal)
                open_heap.push((f[next_state], next(counter) , next_state))
    return None

def solve_AStar_manhattan(start, goal):
    if start is None or goal is None: return None
    state_cnt = 0
    open_heap = MinHeap()
    g = {}; f = {}
    closed = []

    counter = it.count() ## bộ đếm 
    
    g[start] = 0 # giá trị tại ô bắt đầu  tương đương số bước là 0
    f[start] = g[start] + heuristic_manhattan(start,goal)
    open_heap.push((f[start], next(counter) ,start))

    while open_heap.empty() == False:
        cost ,_, state = open_heap.pop()

        if state in closed:
            continue

        if state == goal:
            return state, state_cnt
        
        closed.append(state)

        for dx, dy in actions:
            next_state = generator_state(state, dx, dy)
            state_cnt += 1
            if next_state is None: continue
            cost = g[state] + 1
            if next_state not in g or cost < g[next_state]:
                next_state.parent = state
                g[next_state] = cost
                f[next_state] = g[next_state] + heuristic_manhattan(next_state, goal)
                open_heap.push((f[next_state], next(counter) , next_state))
    return None


def print_step(goal):
    steps = []

    curr = goal
    while curr is not None:
        steps.append(curr)
        curr = curr.parent

    steps.reverse()
    return steps

if __name__ == "__main__":
    start, goal = readfile(debug=globals())
    generator_state(start, -1, 0)
    t1 = time.time()
    #state = solve_UCS(start, goal)

    #print_step(state)
    t2 = time.time()
    print(heuristic_hamming(start, goal))
    print(heuristic_manhattan(start, goal))
    print(t2-t1)
