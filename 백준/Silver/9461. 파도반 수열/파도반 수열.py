import sys

dp = [1]*3
#점화식 N >= 4부터 N = (N-2) + (N-3)
for i in range(3, 100):
    dp.append(dp[i-2] + dp[i-3])

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n-1])