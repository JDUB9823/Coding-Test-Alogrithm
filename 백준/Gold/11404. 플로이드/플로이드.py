import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd():
    for transit in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                graph[start][end] = min(graph[start][transit] + graph[transit][end], graph[start][end])

n = int(input())
m = int(input())
graph = []

for i in range(n+1):
    graph.append([INF] * (n+1))
    graph[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(graph[a][b], cost)

floyd()

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(*graph[i][1:])