import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        for nNode in graph[node]:
            if not visited[nNode]:
                visited[nNode] = True
                q.append(nNode)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
count = 0
for i in range(1, N+1):
    if not visited[i]:
        BFS(i)
        count += 1

print(count)