## 4 8 1 
## 6 3 0
## 2 7 5

## 1 2 3
## 4 5 6
## 7 8 0

import numpy as np
import os

PUZZLE = "D:\ai_pratice_prj\sgu26_csttnt\Tuan03\B3\puzzle.inp"
class State:
    
    def __init__(self, state, parent = None):
        self.state = tuple(tuple(row) for row in state)
        self.parent = parent
        pass

    def to_state(self):
        return self.state
    
    def __eq__(self, other):
        if not isinstance(other, State): return False
        return self.state == other.state
    
    def __repr__(self):
        return f'{self.state}, parent: {self.parent}'
        
    pass

def readfile(debug=None):
    with open(PUZZLE, "rt") as file:
        content = file.readlines()

    start = tuple(tuple(map(int, line.split())) for line in content[0:3])
    goal = tuple(tuple(map(int, line.split())) for line in content[3:6])

    if debug is not None: print("Đọc file thành công!")

    return State(start), State(goal)

def pos0(state):
    s = state.state
    for i, row in enumerate(s):
        for j, x in enumerate(row):
            if x == 0: return i, j

def generator_state(state, dx, dy):
    s = state.state
    cell_list = np.array(s)
    print(cell_list)

#def solve_BFS(start, goal):





if __name__ == "__main__":
    start, goal = readfile(debug=globals())
    generator_state()

