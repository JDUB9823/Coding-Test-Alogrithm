import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
m,k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]
mul = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            mul[i][j] += A[i][l] * B[l][j]

for i in mul:
    print(*i)