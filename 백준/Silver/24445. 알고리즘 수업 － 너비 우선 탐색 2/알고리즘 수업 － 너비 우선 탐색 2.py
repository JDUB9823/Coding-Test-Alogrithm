import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def bfs(v):
    global order
    visited[v] = order
    edges[v].sort(reverse = True)

    for vertex in edges[v]:
        queue.append(vertex)

    while queue:
        vertex = queue.popleft()
        if visited[vertex] == 0:
            order += 1
            bfs(vertex)

n, m, r = map(int, input().split())
visited = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]
queue = deque()
order = 1

for _ in range(m):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

bfs(r)

for i in range(1, n + 1):
    print(visited[i])