import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = []
queue = deque()
queue.append((0, 0))

for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

print(BFS())