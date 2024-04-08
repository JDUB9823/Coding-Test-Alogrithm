import sys
input = sys.stdin.readline

def dfs(v):
    if visited[v] != 0:
        return
    else:
        visited[v] = 1
        for vertex in edges[v]:
            dfs(vertex)

n = int(input())
m = int(input())
visited = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

dfs(1)

print(sum(visited) - 1)