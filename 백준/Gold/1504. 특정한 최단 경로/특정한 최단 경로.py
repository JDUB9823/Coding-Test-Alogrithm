import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        #distance, node
        D, N = heapq.heappop(pq)

        if dist[N] >= D:
            #해당 노드의 인접 노드 탐색
            for next in graph[N]:
                nnode, ndist = next[0], next[1]
                weight = dist[N] + ndist
                #최단거리 갱신 가능의 경우, pq push
                if weight < dist[nnode]:
                    dist[nnode] = weight
                    heapq.heappush(pq, (weight, nnode))

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
nodes = [1, v1, n]
distances = []

for node in nodes:
    #start -> v1, v2 / v1 <-> v2 / end -> v1, v2
    dist = [INF] * (n+1)
    pq = []
    dijkstra(node)
    distances.append(dist)

#res[0] = start -> v1 -> v2 -> end, res[1] = start -> v2 -> v1 -> end
res = [distances[0][v1] + distances[1][v2] + distances[2][v2],
       distances[0][v2] + distances[1][v2] + distances[2][v1]]

if res[0] >= INF and res[1] >= INF:
    print(-1)
else:
    print(min(res))