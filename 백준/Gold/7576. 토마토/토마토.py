import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

def check(res):
    for row in graph:
        for col in row:
            if col == 0:
                return 0
            res = max(res, col)

    return res

m, n = map(int, input().split())
graph = []
queue = deque()
res = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

BFS()
res = check(0)
if res == 0:
    print(-1)
else:
    print(res - 1)
    