from math import sqrt


def SolveMagicSquare(rows, sudoku):
    if sudoku[0][0] != 1 and sudoku[0][0] != 0:
        return 0
    if SolveMagicSquareUtil(rows, sudoku):
        return 1
    else:
        return 0


def SolveMagicSquareUtil(rows, sudoku):
    for i in range(rows):
        for j in range(rows):
            if sudoku[i][j] == 0:
                arr = getPossible(i, j, rows, sudoku)
                while arr:
                    sudoku[i][j] = arr[-1]
                    if check(rows, sudoku) and SolveMagicSquareUtil(rows, sudoku):
                        return True
                    arr.pop()
                return False
    return True


def check(rows, sudoku):
    return check_cols(rows, sudoku) and check_rows(rows, sudoku) and check_small_cell(rows, sudoku)


def getPossible(i, j, rows, sudoku):
    arr = set([l for l in range(1, rows+1)])

    for k in range(rows):
        if sudoku[i][k] in arr:
            arr.remove(sudoku[i][k])

    for k in range(rows):
        if sudoku[k][j] in arr:
            arr.remove(sudoku[k][j])

    return list(arr)

def check_rows(rows, sudoku):

    for row in sudoku:
        check = [0] * (rows + 1)
        for elem in row:
            if elem == 0:
                continue
            if check[elem] != 0:
                return False
            else:
                check[elem] = 1
    return True


def check_cols(rows, sudoku):
    for i in range(rows):
        check = [0] * (rows + 1)
        for elem in [row[i] for row in sudoku]:
            if elem == 0:
                continue
            if check[elem] != 0:
                return False
            else:
                check[elem] = 1
    return True


def check_small_cell(rows, sudoku):

    for start_row in range(0, rows - int(sqrt(rows)), int(sqrt(rows))):
        for start_col in range(0, rows - int(sqrt(rows)), int(sqrt(rows))):
            check = [0] * (rows + 1)
            for i in range(start_row, start_row + int(sqrt(rows))):
                for j in range(start_col, start_col + int(sqrt(rows))):
                    if sudoku[i][j] == 0:
                        continue
                    if check[sudoku[i][j]] != 0:
                        return False
                    else:
                        check[sudoku[i][j]] = 1
    return True


rows = int(input())
cols = int(input())
sudoku = []

for i in range(rows):
    sudoku.append(list(map(int, input().split())))

print(SolveMagicSquare(rows, sudoku))