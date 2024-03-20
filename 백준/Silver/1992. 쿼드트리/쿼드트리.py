def zipVideo(x,y,n):
    global res
    color = video[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if video[i][j] != color:
                color = -1
                break

    if color == -1:
        res += "("
        n = n // 2
        zipVideo(x,y,n)
        zipVideo(x,y+n,n)
        zipVideo(x+n,y,n)
        zipVideo(x+n,y+n,n)
        res += ")"
    elif color == 1:
        res += "1"
    else:
        res += "0"

n = int(input())
video = [list(map(int, input())) for _ in range(n)]
res = ""
zipVideo(0, 0, n)
print(res)
