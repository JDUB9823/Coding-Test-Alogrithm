import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellmanFord(start):
    distance[start] = 0

    #v 횟수 만큼 round 반복
    for i in range(v):
        #round마다 모든 간선 확인
        for j in range(e):
            curNode, nextNode, cost = graph[j]
            #최단거리 갱신 가능의 경우
            if distance[curNode] != INF and distance[nextNode] > distance[curNode] + cost:
                distance[nextNode] = distance[curNode] + cost
                #v-1횟수의 round까지만 값이 갱신됨, v횟수 이후 갱신은 무한 반복
                if i == v-1:
                    return True
    return False

v, e = map(int, input().split())
distance = [INF] * (v+1)
graph = []

for _ in range(e):
    graph.append(list(map(int, input().split())))

if bellmanFord(1):
    print(-1)
else:
    for i in range(2, v+1):
        print(distance[i] if distance[i] != INF else -1)