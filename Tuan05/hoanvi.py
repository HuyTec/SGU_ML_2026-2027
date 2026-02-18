import os

base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "hoanvi.inp")

def readFile(file_path = PATH):
    with open(file = file_path, mode="rt") as file:
        contents =  file.readlines()

    n = int(contents[0].strip())
    comb = [line.strip() for line in contents[1:]]
    return n, comb

def hoanvi(n, comb, debug = False):
    if n < 0: return None
    result = []
    build = []

    def backtracking(build):
        if len(build) == n:
            result.append(build.copy())
            if debug: print(f'result add {build}')
            return
        else:
            for char in comb:
                if char not in build:
                    build.append(char)
                    backtracking(build)
                    a = build.pop()
                    if debug: 
                        print(f'pop: {a}')
                        print(build)

    backtracking(build)
    return result

def in_ketqua(result):
    print(len(result))
    for r in result:
        for c in r:
            print(f'{c} ', end="")
        print()

if __name__ == "__main__":
    n, comb = readFile()
    print(n, comb)
    result = hoanvi(n, comb, debug=True)
    print(result)
    print(len(result))
    pass