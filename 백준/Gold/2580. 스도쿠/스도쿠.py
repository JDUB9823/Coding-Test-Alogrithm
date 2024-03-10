import sys

def checkRow(x, n):
    for i in range(9):
        if board[x][i] == n:
            return False
    return True

def checkCol(y, n):
    for i in range(9):
        if board[i][y] == n:
            return False
    return True

def checkBox(x,y,i):
    for row in range(3):
        for col in range(3):
            if i == board[x//3*3+row][y//3*3+col]:
                return False
    return True

def sudoku(idx):
    #빈 공간을 모두 채운 경우
    if idx == len(blank):
        for i in range(9):
            print(*board[i])
        exit()

    for i in range(1,10):
        x, y = blank[idx][0], blank[idx][1]
        if checkRow(x, i) and checkCol(y, i) and checkBox(x,y,i):
            board[x][y]=i
            sudoku(idx+1)
            #만약 찾은 숫자가 스도쿠를 전부 채울 수 없는 경우
            board[x][y]=0
        
board = []
blank = []
for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if row[j] == 0:
            blank.append([i,j])
    board.append(row)

sudoku(0)