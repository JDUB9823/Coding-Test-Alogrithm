import sys

def checkPosition(pos):
    for i in range(pos):
        #board[pos] == board[i]는 같은 row에 다른 Queen존재 확인
        #abs()는 대각선상의 y좌표, (pos-i)는 대각선상의 x좌표
        if (board[pos] == board[i]) or (abs(board[pos]-board[i]) == (pos - i)):
            return False
    return True

def nQueen(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    else:
        for i in range(N):
            board[idx] = i
            if checkPosition(idx) == True:
                nQueen(idx+1)

N = int(sys.stdin.readline())
#board의 index는 x, value는 y에 해당
board = [0] * N
cnt = 0
nQueen(0)
print(cnt)