#트리 내부 임의의 노드에서 최대 거리에 있는 노드는 트리의 양 끝점 중 하나이다.
# -> 임의의 노드에서 최대 거리에 있는 노드(A)를 구한 후
#    A노드에서 최대 거리에 있는 노드를 구하면? 해당 거리가 트리의 최대 지름이 된다.

import sys
input = sys.stdin.readline

#노드와의 거리는 visited배열에 저장됨
def DFS(node, dist):
    #vertex, weight
    for V, W in tree[node]:
        distSum = dist + W
        if visited[V] == -1:
            visited[V] = distSum
            DFS(V, distSum)

    return

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(N):
    line = list(map(int, input().split()))
    curNode = line[0]
    for i in range(1, len(line) - 1, 2):
        #연결된 노드와 간선의 가중치를 tree에 추가
        tree[curNode].append((line[i], line[i+1]))

#임의의 노드를 1번 노드로 지정
visited[1] = 0
DFS(1, 0)

#임의의 노드인 1번 노드에서의 가장 먼 노드 구하기
maxDist, maxNode = 0, 0
for i in range(1, len(visited)):
    if visited[i] > maxDist:
        maxDist, maxNode = visited[i], i

#찾은 노드에서 가장 먼 노드 구하기
visited = [-1] * (N+1)
visited[maxNode] = 0
DFS(maxNode, 0)

print(max(visited))