import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "xephau.inp")

def readFile(file_path = PATH, debug = True):
    with open(file_path, "rt") as file:
        content = file.readlines()
    n = int(content[0].strip())
    if debug: print("Đọc dữ liệu thành công!")
    pass
    return n

# pos[x] = y: hậu ở vị trí cột x, dòng y
def board(n, pos):
    board = np.zeros((n, n), dtype=int)
    for col in range(len(pos)):
        board[pos[col]][col] = 1
    return board

def print_board(board):
    if board is []: return
    for row in board:
        for col in row:
            if col == 0: print(f'0', end=" ")
            else: print('1', end=" ")
        print()
    print()

def board_to_string(board, showQ = False):
    lines = []
    for row in board:
        line = ""
        for col in row:
            if col == 0:
                if showQ: line += "+ "
                else: line += "0 "
            else:
                if showQ: line += "Q "
                else: line += "1 "
        lines.append(line.rstrip())
    return "\n".join(lines)


def check_valid(row, col, pos):
    for i in range(0, col):
        if pos[i] == row: return False
        if abs(col - i) == abs(row - pos[i]): return False
    return True

#----------------------------------------------------------------------------------------------------------------------
def xephau_bactracking(n, draw_tree = False, queens = False):
    pos = []
    result = []

    tree = nx.DiGraph()

    def backtracking(n, col):
        state_parent = board_to_string(board(n,pos), queens)
        tree.add_node(state_parent, depth =len(pos))

        if col == n:
            result.append(pos.copy())
            return
        else:
            for row in range(0, n):
                if check_valid(row, col, pos): 
                    pos.append(row)
                    
                    state_child = board_to_string(board(n,pos), queens)
                    tree.add_node(state_child, depth = len(pos))
                    tree.add_edge(state_parent, state_child)

                    backtracking(n, col + 1)
                    pos.pop()
            pass
        pass

    backtracking(n=n, col = 0)

    if draw_tree:
        plt.figure(figsize=(10,5))
        layout = nx.multipartite_layout(tree, subset_key="depth")
        nx.draw(tree, layout, with_labels=True,node_color= 'lightgreen',node_shape='s', node_size=500*n, font_size=5+n)
        plt.show()
        pass
    if len(result)==0: 
        print('Vô nghiệm')
        return None
    return result
#-----------------------------------------------------------------------------------------------------------------------
def valid_pairs(row1, col1, row2, col2):
    if row1 == row2: return False
    if abs(col1 - col2) == abs(row1 - row2): return False
    return True

def count_conflicting_pairs(pos): ## Heuristic duy nhất - brute force
    heuristic = 0
    for i in range(0, len(pos)):
        for j in range(i+1, len(pos)):
            if not valid_pairs(pos[i], i, pos[j], j):
                heuristic += 1
            pass
        pass
    return heuristic

def count_conflicts_of_cell(row, col, pos):
    cnt = 0
    for i in range(0, len(pos)):
        if i == col: continue
        if not valid_pairs(row, col, pos[i], i):
            cnt += 1
        pass
    return cnt

def select_random_col(pos):
    collect = [col for col in range(len(pos)) if count_conflicts_of_cell(pos[col], col, pos) > 0]
    return np.random.choice(collect)


def xephau_thamlam(n, step = False):
    pos = [0]*n
    if step: 
        print('Giả sử ban đầu ta đặt các hậu ở hàng 0')
        print(f'pos = {pos}')

    for _ in range(0,n*n):
        h = count_conflicting_pairs(pos)

        if h == 0: 
            if step: 
                print(f'  h = {h}')
                print(board(n, pos))
                print("SUCCESS")
            return pos

        if step: 
            print(f'  h = {h}')
            print(f'{board(n,pos)}')
            print()

        col = select_random_col(pos) ## chọn cột đang xung đột *ngẫu nhiên
        if col is None: return pos

        min_conflicts = 10**9
        selected_best_row = [] 

        for row in range(0,n):
            pos[col] = row
            new_h = count_conflicting_pairs(pos)

            if new_h < min_conflicts:
                min_conflicts = new_h
                selected_best_row = [row]

            elif new_h == min_conflicts:
                selected_best_row.append(row)

        pos[col] = np.random.choice(selected_best_row)
    if step: print("FAILURE")
    return None
  

if __name__ == "__main__":
    n = readFile()
    print(board(4, pos = [0,0,0,0]))
    pass