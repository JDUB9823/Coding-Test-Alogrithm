import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def DFS(x,y):
    if x < 0 or x >= m or y < 0 or y >= n or field[x][y] == 0:
        return
    else:
        field[x][y] = 0
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)

tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                count += 1
                DFS(i,j)
    print(count)