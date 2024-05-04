import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if dist[node] >= weight:
            #인접 노드 탐색
            for nextNode, nextWeight in graph[node]:
                cost = dist[node] + nextWeight

                #최단 거리 갱산
                if cost < dist[nextNode]:
                    dist[nextNode] = cost
                    prev_node[nextNode] = node
                    heapq.heappush(pq, (cost, nextNode))
                

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
prev_node = [0] * (n+1)
path = []

for _ in range(m):
    #start, end, weight
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

start, target = map(int, input().split())

dijkstra(start)

now = target
path = [now]
while now != start:
    now = prev_node[now]
    path.append(now)

print(dist[target])
print(len(path))
print(*path[::-1])