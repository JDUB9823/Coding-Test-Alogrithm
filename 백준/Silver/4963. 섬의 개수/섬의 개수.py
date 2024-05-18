import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y):
    q = deque()
    q.append((x,y))
    dx, dy = [1, -1, 0, 0, 1, -1, 1, -1], [0, 0, -1, 1, -1, 1, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
        

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                BFS(i, j)
                count += 1

    print(count)