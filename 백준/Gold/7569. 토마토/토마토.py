import sys
from collections import deque
input = sys.stdin.readline


def BFS():
    dz, dy, dx = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))


def check(res):
    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    return 0
                res = max(res, k)
    return res


m, n, h = map(int, input().split())
graph = []
queue = deque()

for _ in range(h):
    level = []
    for _ in range(n):
        level.append(list(map(int, input().split())))
    graph.append(level)

#높이, 세로, 가로
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

BFS()
res = check(0)
if res == 0:
    print(-1)
else:
    print(res - 1)