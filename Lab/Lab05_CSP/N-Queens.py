# Bài toán đặt N quân hậu trên bàn cờ NxN (với N là số tự nhiên >= 4)

import numpy as np
import random as rd
import matplotlib.pyplot as plt

'''
Cài đặt theo hướng đặt hậu theo từng hàng
## Ta có các ô ko thể đặt nếu đã đặt dòng trước đó một hậu ở (i,j) với k là hằng số ta có:
## Chéo chính: (i+k, j+k), chéo phụ: (i+k, j-k), cột dọc: (i+k, j)
## Tại mỗi ô (x,y) so với (i,j) thì nếu:
## Trùng đường chéo chính: có x = y + k và (x,y) = (i+k,j+k) 
#                                   => x-i = k và y-j = k 
#                                   => x-i = y-j = k
#                                   =>|x-i| = |y-j| = k

## Trùng đường chéo phụ : x = k-y và (x,y) = (i+k,j-k) 
#                                   => x-i = k và y-j = -k <=> |y-j| = k
#                                   => x-i = |y-j| = k
#                                   => |x-i| = |y-j| = k
 
## Suy ra tổng quát: Trùng cả hai chéo: |x-i| = |y-j| = k
## Trùng dọc: chỉ số cột bằng nhau
'''

def parseBoard(pos):
    N = len(pos)
    board = np.full((N,N),".", dtype='<U3')
    for r, c in enumerate(pos):
        board[r][c] = "Q"
    for r in range(len(board)):
        for c in range(len(board[r])):
            print(f'{board[r][c]}', end=" ")
        print()

#=================== Quay lui ==================================================

def check_valid(row, col, pos): ## kiểm tra vùng tấn công
    for i in range(0, row):
        if pos[i] == col: return False
        if abs(row - i) == abs(col - pos[i]): return False
    return True


def backtracking_recursion(row, N, pos, counter):
    if row == N:
        counter[0] += 1
        print(f"Way {counter[0]}:")
        parseBoard(pos)
        print()
        return 1
    count = 0
    for col in range (0, N):
        if check_valid(row, col, pos):
            pos.append(col)
            count += backtracking_recursion(row+1, N, pos, counter) # đệ quy
            pos.pop() # backtracking trả về trạng thái cũ
    return count

def N_Queens(N):
    pos = []  ## Tương ứng pos[i] = k (đặt hậu vị trí cột k dòng i)
    counter = [0]
    count = backtracking_recursion(0, N, pos, counter)
    parseBoard(pos)
    print(f'Bàn cờ {N}x{N} có {count} cách đặt {N} quân hậu không tấn công nhau')

#==================Theo nguyên lý heuristic (Min conflicts)======================================
def conflicts_counter(row, col, pos):
    N = len(pos)
    cnt = 0
    for i in range(0,N):
        if i == row: continue
        if abs(row - i) == abs(pos[i] - col) or pos[i] == col:
            cnt+=1
    return cnt

def cnt_conflicts_pairs(pos):
    h = 0
    N = len(pos)
    for i in range(N):
        for j in range(i+1, N):
            if pos[i] == pos[j] or abs(i-j) == abs(pos[i]-pos[j]):
                h+=1
    return h

def select_row(pos):
    collect = [row for row in range(len(pos)) if conflicts_counter(row, pos[row], pos) > 0]
    if not collect: return None
    return rd.choice(collect)


def N_Queens_H(N, verbose = True):
    ## Giả sử đặt N quân hậu tất cả ở cột đầu tiên
    pos = [rd.randint(0, N-1) for _ in range(N)]
    maxStep = 100*N

    for step in range(1, maxStep):
        h = cnt_conflicts_pairs(pos)
        if verbose: print(f'\nStep {step}, conflict h = {h}')
        parseBoard(pos)
        if h == 0:
            print(f'Found sulution!')
            return pos
        row = select_row(pos)
        if row is None: return None
        min_conf = 10**9
        best_col = []
        for col in range(0,N):
            conf = conflicts_counter(row, col, pos)
            if conf < min_conf:
                min_conf = conf
                best_col = [col]
            elif conf == min_conf:
                best_col.append(col)

        pos[row] = rd.choice(best_col) 
    return None

    
if __name__ == "__main__":
    n = 8
    pos2 = N_Queens(n)
    
    pos = N_Queens_H(n)
    parseBoard(pos)




