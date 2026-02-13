import random
import os

base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "madituan.inp")

def readFile(file_path = PATH, debug = True):
    with open(file_path, "rt") as file:
        content = file.readlines()

    l = list(map(int, content[0].split()))
    n = l[0]
    x0 = l[1]
    y0 = l[2]
    if debug: print("Đọc dữ liệu thành công!")
    return n, x0, y0


actions = [[-2,-1],[2,-1],[-1,-2],[1,-2],[-2,1],[2,1],[-1,2],[1,2]]
"""-------------------------------------------------------------------------"""

def bac(n, x, y, board):
    cnt = 0
    for dx, dy in actions:
        x_n = x + dx
        y_n = y + dy
        if 0 <=  x_n < n and 0 <= y_n < n and  board[x_n][y_n] == 0:
            cnt += 1
    return cnt

def sapxep_luachon(n, x, y, board):
    candicates = []
    for dx, dy in actions:
        x_n = x + dx
        y_n = y + dy
        if 0 <= x_n < n and 0 <= y_n < n and board[x_n][y_n] == 0:
            candicates.append((bac(n, x_n, y_n, board), x_n, y_n))
    candicates.sort()
    return candicates
    

"""-------------------------------------------------------------------------"""

def madituan_bactracking(n, x0, y0, limit = (False, 1000000)): ## x0, y0 base 1
    if n % 2 == 1 or n < 6: return None
# n=3, n=4, n=5 ko có lời giải, không có chu trình Hamilton
    x0 -= 1
    y0 -= 1

    if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n:
        return None
    
    result = []
    counter = 0

    board = [[0]*n for _ in range(n)]
    board[x0][y0] = 1

    def backtracking(x, y):
        nonlocal counter
        if limit[0]:
            counter += 1
            if counter > limit[1]: return False
        
        choices = sapxep_luachon(n, x, y, board)

        # if board[x][y] == n**2 - 1:             ## tại bước gần cuối kiểm tra ô tiếp có thể khả thi đi về lại ô bắt đầu
        #     possible = []
        #     for deg, nx, ny in choices:
        #         for dx, dy in actions:
        #             if nx + dx == x0 and ny + dy == y0:
        #                 possible.append((deg,nx,ny))
        #     if not possible: return False
        #     choices = possible
        #     if not choices: return False
    
        if board[x][y] == n*n:
            for dx, dy in actions:
                if x + dx == x0 and y + dy == y0:
                    result.append([row[:] for row in board])
                    return True
            return False
        
        for _, x_n, y_n in choices:
            board[x_n][y_n] = board[x][y] + 1
            if backtracking(x_n, y_n):
                    return True
                
            board[x_n][y_n] = 0
            pass
        return False

    backtracking(x0, y0)
    if limit[0]: 
        print(f"Đã giới hạn đệ quy với {limit[1]} phép tính toán: ")
        if len(result) == 0: print("Vẫn chưa tìm được lời giải")
        else: print(result)
    return result

"""-------------------------------------------------------------------------"""
def uu_tien(n, x, y, board):
    choice = sapxep_luachon(n, x, y, board)
    if not choice:
        return False
    a, _, _ = choice[0]
    collect = [(deg, x, y) for (deg,x,y) in choice if deg == a]
    if len(collect) == 1: return (collect[0])
    return random.choice(collect)

def madituan_heuristic(n, x0, y0, try_step = False): #Quy tắc của Warnsdorf
    if n % 2 == 1 or n < 6: return None # n=3, n=4, n=5 ko có lời giải, không có chu trình Hamilton
    x0 -= 1
    y0 -= 1
    if x0 < 0 or x0 >= n or y0 < 0 or y0 >= n:
        return None
    time = 0

    while True:
        time += 1
        if try_step: print(f'{time} times try', end=": ")

        board = [[0]*n for _ in range(n)]
        board[x0][y0] = 1

        cnt = 1
        x = x0; y = y0
        while cnt < n**2:
            if cnt == n**2 - 1:             ## tại bước gần cuối kiểm tra ô tiếp có thể khả thi đi về lại ô bắt đầu
                choices = sapxep_luachon(n, x, y, board)

                possible = []
                for deg, nx, ny in choices:
                    for dx, dy in actions:
                        if nx + dx == x0 and ny + dy == y0:
                            if try_step: print("found correct solution")
                            possible.append((deg,nx,ny))
                if not possible: break
    
                choice = min(possible)
            else:          
                choice = uu_tien(n, x, y, board)
                if not choice:
                    break

            _ ,x ,y = choice
            cnt += 1
            board[x][y] = cnt
            pass
        if cnt == n**2:
            for dx, dy in actions:
                if x + dx == x0 and y + dy == y0:
                    if try_step: print("success")
                    return board
        if try_step: print("fail")
                
if __name__ == "__main__":
    n, x0, y0 = readFile()
    print(n, x0, y0)
    n = 10
    board2 = madituan_heuristic(n, x0, y0)

    if board2 is None:
        print("Không tìm được lời giải")
    else:
        for row in range(n):
            for col in range(n):
                print(f'{board2[row][col]:3}', end=" ")
            print()
    pass