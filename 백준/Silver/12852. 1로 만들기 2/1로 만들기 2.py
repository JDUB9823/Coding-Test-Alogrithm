import sys

x = int(sys.stdin.readline())
DP = [0] * (x+1)
path = [[] for _ in range(x+1)]
path[1] = [1]
    
for idx in range(2, x+1):
    DP[idx] = DP[idx-1] + 1
    prev = idx - 1

    if idx % 3 == 0 and DP[idx//3] < DP[idx]:
        DP[idx] = DP[idx//3] + 1
        prev = idx // 3

    if idx % 2 == 0 and DP[idx//2] < DP[idx]:
        DP[idx] = DP[idx//2] + 1
        prev = idx // 2
        
    path[idx] = path[prev] + [idx]

print(DP[x])
print(*path[x][::-1])