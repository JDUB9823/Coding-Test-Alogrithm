import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
res = 0

for i in range(n):
    bMax = max(B)
    res += A[i] * bMax
    B.remove(bMax)

print(res)