def cutPaper(x,y,n):
    check = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != check:
                n = n // 3
                cutPaper(x,y,n)
                cutPaper(x+n,y,n)
                cutPaper(x+2*n,y,n)
                cutPaper(x,y+n,n)
                cutPaper(x+n,y+n,n)
                cutPaper(x+2*n,y+n,n)
                cutPaper(x,y+2*n,n)
                cutPaper(x+n,y+2*n,n)
                cutPaper(x+2*n,y+2*n,n)
                return

    if check == -1:
        res[0] += 1
    elif check == 0:
        res[1] += 1
    else:
        res[2] += 1
    return

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res = [0] * 3
cutPaper(0,0,n)
for r in res:
    print(r)