import sys
from collections import deque
input = sys.stdin.readline

def DFS(v):
    if DFS_visited[v] != 0:
        return
    else:
        DFS_visited[v] = 1
        DFS_res.append(v)
        for vertex in edges[v]:
            DFS(vertex)
    return

def BFS(v):
    if BFS_visited[v] != 0:
        return
    else:
        BFS_visited[v] = 1
        BFS_res.append(v)
        for vertex in edges[v]:
            queue.append(vertex)
        while queue:
            BFS(queue.popleft())
    return

n, m, v = map(int, input().split())
DFS_visited, BFS_visited = [0] * (n + 1), [0] * (n + 1)
DFS_res, BFS_res = [], []
edges = [[] for _ in range(n + 1)]
queue = deque()

for _ in range(m):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

for i in range(1, n+1):
    edges[i].sort()

DFS(v)
BFS(v)
print(*DFS_res)
print(*BFS_res)