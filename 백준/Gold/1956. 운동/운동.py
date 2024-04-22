import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd():
    for transit in range(1, v+1):
        for start in range(1, v+1):
            for end in range(1, v+1):
                graph[start][end] = min(graph[start][end], graph[start][transit] + graph[transit][end])

v, e = map(int, input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

floyd()
res = INF

for i in range(1, v+1):
    for j in range(1, v+1):
        res = min(graph[i][j] + graph[j][i], res)

print(res if res < INF else -1)