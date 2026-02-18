import os

# .....2.3.
# 374..6.2.
# .....8.1.
# 258......
# .........
# ......493
# .4.1.....
# .2.8..675
# .6.5.....
base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "fujiwara.inp")

def readFile(file_path = PATH):
    with open(file_path, "rt") as file:
        contents = file.readlines()

    sodoku = [[-1]*9 for _ in range(9)]

    for i, line in enumerate(contents):
        for j, char in enumerate(line.strip()):
            if char == ".":
                continue
            sodoku[i][j] = int(char)-1
            pass
        pass
    return sodoku

def sudoku_board(board, hide=False, based0=False):
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if hide and val == -1:
                print(" .", end=" ")
            else:
                if not based0:
                    val += 1
                print(f"{val:2}", end=" ")
        print()
    print()


def state_debug(box, row, col):
    print('box: ')
    for i in range(9):
        print(bin(box[i]))

    print('row: ')
    for i in range(9):
        print(bin(row[i]))
        
    print('col: ')
    for i in range(9):
        print(bin(col[i]))
    pass

"""
PP1: Phương pháp BIT-MASKING (Sử dụng các phép toán bitwise)
** Lưu ý ở đây làm theo 0-based (chỉ số bắt đầu từ 0)
row[i]  có bit k = 1  → số k đã xuất hiện ở hàng i
col[j]  có bit k = 1  → số k đã xuất hiện ở cột j
box[b]  có bit k = 1  → số k đã xuất hiện ở box b

** để lấy chỉ số box dựa trên tọa độ (dòng,cột) = (i,j)
    b = (i//3) *3 + j//3  (với // là chia lấy nguyên)

Không trùng với các số khác tại [i,j] sử dụng phép or để đánh dấu số đã tồn tại trong dòng, cột, hộp: used = row[i] or col[j] or box[b]
available = f and not used
với mỗi phần tử trong 3 mảng bitmask sẽ trên thao tác trên bit có độ dài 9 (bit 0 to 8) để đánh dấu các số đã tồn tại
* Với việc chọn số khả thi tiếp theo để điền:
Giả sử ta có bit lưu các số đã tồn tại: mask = 00100110 (nếu số có thể điền là 1,2,5)
~mask = 11011001
=> -mask:
        11011001
    &          1
    ------------
        11011010

=> mask & -mask:
        00100110
    &   11011010
    -------------
        00000010  tương ứng với số 1 (số nhỏ nhất)

    tắt bit vừa xét để đến bit tiếp theo
    tiếp tục lặp cho đến khi mask = 0 để lấy ra 

*VÍ DỤ:  xét tại ô [0,0] (i=0, j=0, b=0)
        dòng 0 đã tồn tại các số: 0, 4, 8   => row[0] = 100010001 (từ phải sang trái)
        cột 0 đã tồn tại các số: 1, 4, 6    => col[0] = 001010010
        hộp 0 đã tồn tại các số: 1, 2, 4    => box[0] = 000010110
                                                       -----------
        => used = row[0] or col[0] or box[0]    =       101010110  (Tương ứng với 1,2,4,6,8 đã tồn tại)
        
        => available = f and not used   = 111111111 and not 101010110  (phép not là đảo ngược bit)
                                        = 111111111 and     010101001
                                        = 010101001 (Tương ứng với các số có thể điền là 7,5,3,0)

PP2: Phương pháp tối ưu MRV (Minimum Remaining Value):
    Lựa chọn ưu tiên điền các ô có số lượng các số khả thi là thấp nhất (dễ rơi vào bế tắc nhất)

PP3: Phương pháp Backtracking (Quay lui tìm kiếm)
backtracking()
    Thực hiện đệ quy sử dụng kết hợp 2 phương pháp trên.
    chọn ô i, j dễ bế tắc (MRV)
    tại ô i,j: thử với các số khả thi của nó:
        đặt số vào ô
        backtracking()
        gỡ số vừa đặt

"""
def find_best_start(board, box, row, col): ## nếu trả về NONE nghĩa là không tìm đc min nữa, đồng nghĩa tất cả ô đã điền hết
    min_cnt = 10 # nếu tất cả số
    full = (1 << 9) - 1 #bit : 10000000000 - 1 = 0111111111
    best = None
    for i in range(9):
        for j in range(9):
            if board[i][j] != -1:
                continue
            used = row[i]|col[j]|box[(i//3)*3+j//3]
            available = (full & ~used)
            avai_cnt =  available.bit_count()

            if avai_cnt < min_cnt:
                min_cnt = avai_cnt
                best = (i, j ,available)

                if avai_cnt == 1: return (i, j, available)## đã tốt nhất vì ô không còn lựa chọn nào khác
            pass
        pass
    return best

def place(i, j, num, board, box, row, col): # hàm đặt số vào ô (i, j) với giá trị num
    box[(i//3)*3+j//3] |= (1 << num)
    col[j] |= (1 << num)
    row[i] |= (1 << num)
    board[i][j] = num
    pass

def remove(i, j, board, box, row, col): # gỡ số khỏi ô (i,j)
    box[(i//3)*3+j//3] ^= (1 << board[i][j])
    col[j] ^= (1 << board[i][j])
    row[i] ^= (1 << board[i][j])
    board[i][j] = -1
    pass

## Hướng giải quyết, thủ thuật bitmasking và MRV (chọn ô có ít lựa chọn để đi trước)
def solver(board):
    result = []
    box = [0]*9
    row = [0]*9
    col = [0]*9

    for i in range(9):
        for j in range(9):
            if board[i][j] != -1:
                box[(i//3)*3+j//3] |= (1 << board[i][j])
                col[j] |= (1 << board[i][j])
                row[i] |= (1 << board[i][j])
                pass
            pass
        pass
    
    def backracking():
        start = find_best_start(board, box, row, col)
        if start is None: 
            result.append([row[:] for row in board])
            return True
        i, j, available = start

        while available:
            bit = available & -available
            num = bit.bit_length() - 1
            place(i, j, num, board, box, row, col)
            if backracking(): return True
            remove(i, j, board, box, row, col)
            available ^= bit
            pass
        return False

    backracking()
    return result

if __name__ == "__main__":
    sodoku  = readFile()
    sudoku_board(sodoku, hide = False, based0=False)



    board = solver(sodoku)
    sudoku_board(board[0], hide = False, based0=False)

    # mask = 0
    # print(bin(mask), mask) #0b0 và 0
    # mask |= (1<<8) ##đặt bit1 ở bit thứ 8 đếm từ 0
    # print(bin(mask), mask) #0b100000000 và 2^8 = 256
    # mask |= (1<<3) 
    # ##0b đánh dấu cho Python là số nhị phân, phía sau là dãy nhị phân
    # print(bin(mask), mask) #0b100001000 và 2^8 + 2^3 = 264
    # print(mask & (1<<8))
    # print(bin(mask), mask) #0b100001000 và 2^8 + 2^3 = 264
    # n = 8
    # for i in range(n+1):
    #     if mask & (1 << i):
    #         print(i)
    pass