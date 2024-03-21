import sys
input = sys.stdin.readline

def mul(a,b,n):
    m = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m[i][j] += a[i][k] * b[k][j] % 1000
    return m

def square(a,b,n):
    if b == 1:
        return a
    else:
        temp = square(a,b//2,n)
        if b % 2 == 0:
            return mul(temp,temp,n)
        else:
            return mul(mul(temp,temp,n),a,n)
        

n,b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

res = square(A,b,n)
for i in range(n):
    for j in range(n):
        res[i][j] %= 1000

for row in res:
    print(*row)