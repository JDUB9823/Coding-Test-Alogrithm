import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        #Distance, Node
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
    
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
pq = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

dijkstra(K)

for i in range(1, V+1):
    print(dist[i] if dist[i] != INF else "INF")