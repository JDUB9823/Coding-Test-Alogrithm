import sys
input = sys.stdin.readline

#m번 사건에서 n번 사건으로 이동하는 거리
def getDistance(m, n):
    return abs(pos[m][0] - pos[n][0]) + abs(pos[m][1] - pos[n][1])

def DP(m, n):
    #next case
    nCase = max(m, n) + 1

    if nCase == W + 2:
        return 0

    if dp[m][n] != -1:
        return dp[m][n]

    dist1 = DP(nCase, n) + getDistance(m, nCase)
    dist2 = DP(m, nCase) + getDistance(n, nCase)

    if dist1 < dist2:
        path[m][n] = 1
        dp[m][n] = dist1
    else:
        path[m][n] = 2
        dp[m][n] = dist2

    return dp[m][n]
    

N = int(input())
W = int(input())
pos = [[1,1], [N,N]] +[list(map(int, input().split())) for _ in range(W)]
dp = [[-1] * (W+1) for _ in range(W+1)]
path = [[0] * (W+1) for _ in range(W+1)]

print(DP(0,1))

m, n = 0, 1
for i in range(2, W+2):
    print(path[m][n])
    if path[m][n] == 1:
        m = i
    else:
        n = i