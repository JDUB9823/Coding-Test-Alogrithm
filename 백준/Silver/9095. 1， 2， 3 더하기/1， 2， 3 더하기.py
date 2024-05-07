t = int(input())
dp = [0] * (11)
dp[1:4] = [1,2,4]

for i in range(4, 11):
    dp[i] = sum(dp[i-3:i])

for _ in range(t):
    n = int(input())
    print(dp[n])