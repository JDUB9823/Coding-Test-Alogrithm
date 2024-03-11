import sys
input = sys.stdin.readline

N = int(input())
dp = []
for i in range(N):
    level = list(map(int, input().split()))
    if i != 0:
        for j in range(len(level)):
            #삼각형의 맨 끝인 경우
            if j == 0:
                level[j] += dp[i-1][j]
            elif j == len(level)-1:
                level[j] += dp[i-1][j-1]
            else:
                level[j] += max(dp[i-1][j-1], dp[i-1][j])
    dp.append(level)

print(max(dp[-1]))