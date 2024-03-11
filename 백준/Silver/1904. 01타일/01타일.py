import sys

n = int(sys.stdin.readline())
dp = [1] + [2] + [0] * 999999

for k in range(2,n):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n-1])