import sys
input = sys.stdin.readline

N = int(input())
dp = []
for i in range(N):
    r,g,b = map(int, input().split())
    if i == 0:
        dp.append([r,g,b])
    else:
        dp.append([
            r + min(dp[i-1][1], dp[i-1][2]),
            g + min(dp[i-1][0], dp[i-1][2]),
            b + min(dp[i-1][0], dp[i-1][1])])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))