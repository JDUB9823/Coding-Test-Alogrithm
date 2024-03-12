import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
dp = [1] * 1001

for i in range(N):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))