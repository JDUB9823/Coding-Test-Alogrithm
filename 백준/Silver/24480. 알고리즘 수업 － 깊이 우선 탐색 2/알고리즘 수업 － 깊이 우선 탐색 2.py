import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(v):
    global order
    visited[v] = order
    edges[v].sort(reverse = True)

    for vertex in edges[v]:
        if visited[vertex] == 0:
            order += 1
            dfs(vertex)

n, m, r = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
order = 1

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])