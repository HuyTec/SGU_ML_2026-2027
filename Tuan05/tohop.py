import os

base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "tohop.inp")


def readFile(filepath = PATH, verbose = True):
    with open(filepath, "rt") as file:
        content = file.readlines()

    n, k = map(int, content[0].split())
    combination = [line.strip() for line in content[1:]]  ## đọc từng line trong content[1] lấy các ký tự trong tổ hợp, strip() xóa space đầu cuối
    if verbose: print("Data file read successfully!")
    return n, k, combination


def print_result(result):
    if not result: print(None)
    print(len(result))
    for r in result:
        for sym in r:
            print(f'{sym}', end = "")
        print()
    pass

def backtracking(n, k, result, build, combination, start, debug = False):
    if debug: 
        print(f'{build}')

    if len(build) == k:
        result.append(build.copy())
        if debug: print(f'Các tổ hợp: {result}\n')
        return
    else:
        for i in range(start, n):
            build.append(combination[i])
            backtracking(n, k, result, build, combination, i+1, debug)
            a = build.pop()
            if debug: 
                print(f'pop: {a}')
                print(build)

def combine(n, k, combination, debug = False):
    if (k > n): return None
    result = []
    
    backtracking(n, k, result, [], combination, 0, debug)
    if debug: 
        print(f'Số lượng tổ hợp: {len(result)}')
        print(result)
    return result


if __name__ == "__main__":
    n,k,comb = readFile(PATH)
    print(n,k,comb)

    pass