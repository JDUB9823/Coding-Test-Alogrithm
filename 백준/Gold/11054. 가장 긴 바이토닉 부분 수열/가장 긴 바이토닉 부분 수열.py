import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
dpUp = [1 for _ in range(N)]
dpDown = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num[i] > num[j]:
            dpUp[i] = max(dpUp[i], dpUp[j]+1)
    for k in range(N-i, N):
        idx = N-i-1
        if num[idx] > num[k]:
            dpDown[idx] = max(dpDown[idx], dpDown[k]+1)

print(max([x+y for x,y in zip(dpUp, dpDown)])-1)