import sys
input = sys.stdin.readline

def getCount(PS):
    count = 4000000
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            count = min(count, PS[i+k-1][j+k-1]-PS[i+k-1][j-1]-PS[i-1][j+k-1]+PS[i-1][j-1])
    return count

def paintBoard(color):
    PS = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                if board[i][j] == color:
                    val = 1
                else:
                    val = 0
            else:
                if board[i][j] != color:
                    val = 1
                else:
                    val = 0
            PS[i+1][j+1] = PS[i][j+1] + PS[i+1][j] - PS[i][j] + val

    return getCount(PS)

n,m,k = map(int, input().split())
board = []
for _ in range(n):
    row = list(input().rstrip())
    board.append(row)

print(min(paintBoard("W"), paintBoard("B")))