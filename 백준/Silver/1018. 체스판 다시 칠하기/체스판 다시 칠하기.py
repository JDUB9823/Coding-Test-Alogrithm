def checkBoard(x, y):
    bwCount, wbCount = 0, 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if board[i][j] != bwBoard[i-x][j-y]:
                bwCount += 1
            if board[i][j] != wbBoard[i-x][j-y]:
                wbCount += 1

    return min(bwCount, wbCount)

N, M = map(int, input().split())
board = []

for _ in range(N):
    row = input()
    board.append(row)

bwBoard = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
wbBoard = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]

count = 64
for i in range(0, N-7):
    for j in range(0, M-7):
        count = min(count, checkBoard(i, j))

print(count)