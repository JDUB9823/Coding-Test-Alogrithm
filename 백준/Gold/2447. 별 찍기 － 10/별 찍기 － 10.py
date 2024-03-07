def fillblank(board, x, y, size):
    for i in range(size):
        for j in range(size):
            board[x+i][y+j] = " "
    
N = int(input())
#NxN 배열을 모두 *로 채운다
board = [["*" for _ in range(N)] for _ in range(N)]
#size x size = 공백을 그려야 하는 크기
size = N//3

while True:
    if size < 1:
        break
    #x, y는 " "로 바꿀 board의 왼쪽 상단 위치로 초기화
    x, y = size, size

    #size * 3만큼 indexing을 통해 다음 공백의 위치 지정
    for i in range(x,N,size*3):
        for j in range(y,N,size*3):
            fillblank(board,i,j,size)
    #해당 size만큼의 공백이 모두 그려지면, 다음 공백의 size로 감소
    size //= 3

for i in range(N):
    for j in range(N):
        print(board[i][j], end="")
    print()