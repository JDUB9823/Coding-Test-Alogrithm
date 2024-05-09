import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd():
    for transit in range(n):
        for start in range(n):
            for end in range(n):
                transitCost = graph[start][transit] + graph[transit][end]
                if transitCost < graph[start][end]:
                    graph[start][end] = transitCost
                    #최단경로 기록
                    path[start][end] = path[start][transit] + path[transit][end][1:]

n = int(input())
m = int(input())
graph = []
path = [[()] * (n) for _ in range(n)]

for _ in range(n):
    graph.append([INF] * (n))
    graph[_][_] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
    path[a-1][b-1] = (a, b)

floyd()

#최단거리 출력
for row in graph:
    for value in row:
        print(value if value != INF else 0, end=" ")
    print()

#최단경로 출력
for i in range(n):
    for j in range(n):
        print(len(path[i][j]), *path[i][j])