import sys
#dp[N][M] (N<=M)
#f(N,M) = dp[i-1][j-1] + dp[i][j-1]

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    #N = 1일때
    for i in range(1, M+1):
        dp[1][i] = i

    #N >= 2일때
    for i in range(2, N+1):
        for j in range(i, M+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    print(dp[N][M])