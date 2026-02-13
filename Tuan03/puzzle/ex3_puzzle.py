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


def solve_BFS(start, goal):
    if start is None or goal is None: return None
    state_cnt = 0
    queue = deque()
    visited = set()
    closed = []

    visited.add(start)
    queue.append(start)

    while len(queue)>0:
        state = queue.popleft() ## FIFO Queue

        if state == goal:
            return state, state_cnt
        closed.append(state)

        for dx, dy in actions:
           
            next_state = generator_state(state, dx, dy)
            if next_state is None: continue
            state_cnt += 1
            if next_state not in visited:
                visited.add(next_state)
                next_state.parent = state
                queue.append(next_state)
    return None

def solve_DFS(start, goal):
    if start is None or goal is None: return None
    state_cnt = 0
    stack = deque()
    visited = set()
    closed = []

    visited.add(start)
    stack.append(start)

    while len(stack)>0:
        state = stack.pop() ## LIFO Stack

        if state == goal:
            return state, state_cnt
        closed.append(state)

        for dx, dy in actions:
            next_state = generator_state(state, dx, dy)

            if next_state is None: continue
            state_cnt += 1
            if next_state not in visited:
                visited.add(next_state)
                next_state.parent = state
                stack.append(next_state)
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
    state = solve_DFS(start, goal)

    print_step(state)
    t2 = time.time()

    print(t2-t1)
