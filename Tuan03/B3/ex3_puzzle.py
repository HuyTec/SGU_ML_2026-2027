## 4 8 1 
## 6 3 0
## 2 7 5

## 1 2 3
## 4 5 6
## 7 8 0

import numpy as np
import os

FI = "puzzle.inp"
class State:
    
    def __init__(self, key, parent = None, cost = 0):
        self.key = [[v for v in row] for row in key]
        self.parent = parent
        self.cost = cost
        pass
    def tokey(self):
        return tuple([tuple([v for v in row])for row in self.key])
    pass
def solve(debug=None):
    with open(FI, "rt") as file:
        content = file.readlines()

    # đọc 3 dòng đầu làm trạng thái start
    start = []
    for row in content[0:3]:
        start.append([v.replace('\n','') for v in row.split(' ')])

    goal = []
    for row in content[3:6]:
        start.append([v.replace('\n','') for v in row.split(' ')])

    start = np.array(start)
    goal = np.array(goal)

    print(State(start))

    if debug is not None:
        debug.update(locals())

if __name__ == "__main__":
    solve(debug=globals())

