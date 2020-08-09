# 检查这个数能不能填
def check(sudoku, i, j):
    cur = sudoku[i][j]
    for k in range(9):
        if k != i and sudoku[k][j] == cur:
            return False
        if k != j and sudoku[i][k] == cur:
            return False
        if (k//3 != i%3 or k%3 != j%3) and sudoku[i//3*3+k//3][j//3*3+k%3] == cur:
            return False
    return True

# 回溯法，对第一个空位尝试填空
# 都不对说明前面有错，改回0
def solve(sudoku):
    flag = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        return True
    for k in range(1, 10):
        sudoku[i][j] = k
        if not check(sudoku, i, j):
            continue
        flag = solve(sudoku)
        if flag == True:
            return True
    sudoku[i][j] = 0
    return False

while True:
    try:
        sudoku = []
        for i in range(9):
            line = list(map(int, input().split()))
            sudoku.append(line)
        solve(sudoku)
        for line in sudoku:
            print(' '.join(map(str, line)))
    except:
        break
