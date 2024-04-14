import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    while queue:
        x, y, isbreak = queue.popleft()
        if x == n-1 and y == m-1:
            return DP[n-1][m-1][isbreak]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            #다음 움직임이 맵의 범위 안에 포함
            if 0 <= nx < n and 0 <= ny < m and DP[nx][ny][isbreak] == 0:
                #다음 move가 벽인 경우, 벽을 부신 경로에 + 1
                if graph[nx][ny] == 1 and isbreak == 0:
                    DP[nx][ny][1] = DP[x][y][isbreak] + 1
                    queue.append((nx, ny, 1))
                #다음 move가 벽이 아니고, 이전에 방문하지 않은 경우
                if graph[nx][ny] == 0 and DP[nx][ny][isbreak] == 0:
                    DP[nx][ny][isbreak] = DP[x][y][isbreak] + 1
                    queue.append((nx, ny, isbreak))
    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
#DP[x][y][0] = 벽을 안 부신 경로, DP[x][y][1] = 벽을 부신 경로
DP = [[[0, 0] for _ in range (m)] for _ in range(n)]
DP[0][0][0] = 1
queue = deque([(0, 0, 0)])

print(BFS())