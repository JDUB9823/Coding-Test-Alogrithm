import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y):
    dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [1, -1, 2, -2, 2, -2, 1, -1]
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        if x == targetx and y == targety:
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[targetx][targety]

tc = int(input())
for _ in range(tc):
    l = int(input())
    x, y = map(int, input().split())
    targetx, targety = map(int, input().split())
    graph = [[0] * l for _ in range(l)]

    print(BFS(x, y))