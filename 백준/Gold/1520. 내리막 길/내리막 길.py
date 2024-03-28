import sys
input = sys.stdin.readline

def findPath(x, y):
    #지도의 맨 끝에 도착한 경우
    if x == m-1 and y == n-1:
        return 1
    #해당 위치를 방문하지 않은 경우
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            if 0 <= nextX < m and 0 <= nextY < n and levels[x][y] > levels[nextX][nextY]:
                dp[x][y] += findPath(nextX, nextY)
    
    return dp[x][y]
    
m, n = map(int, input().split())
levels = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
#다음 x,y가 가야할 방향
dx, dy = [1,0,-1,0], [0,1,0,-1]
print(findPath(0, 0))