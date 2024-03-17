import sys
input = sys.stdin.readline

N, M = map(int, input().split())
PS = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    row = [0] + list(map(int, input().split()))
    for j in range(1,N+1):
        PS[i][j] = PS[i-1][j] + PS[i][j-1] - PS[i-1][j-1] + row[j]

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    print(PS[x2][y2] - PS[x2][y1-1] - PS[x1-1][y2] + PS[x1-1][y1-1])