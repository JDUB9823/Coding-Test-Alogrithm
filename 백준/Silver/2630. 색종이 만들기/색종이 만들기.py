import sys
input = sys.stdin.readline

def cutPaper(x,y,n):
    global blue, white
    #왼쪽 상단 색종이의 색
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            #색이 다른 경우
            if paper[i][j] != color:
                s = n//2
                cutPaper(x, y, s)
                cutPaper(x, y+s, s)
                cutPaper(x+s, y, s)
                cutPaper(x+s, y+s, s)
                return

    if color == 1:
        blue += 1
    else:
        white += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0
cutPaper(0, 0, n)

print(white)
print(blue)