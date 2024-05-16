import sys
from collections import deque
input = sys.stdin.readline

def BFS(root):
    visited = [-1] * (N+1)
    visited[root] = 0
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        for nNode, nCost in tree[node]:
            if visited[nNode] == -1:
                visited[nNode] = visited[node] + nCost
                q.append(nNode)

    res = max(visited)
    return (visited.index(res), res)

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    #parent, child, weight
    P, C, W = map(int, input().split())
    tree[P].append((C, W))
    tree[C].append((P, W))

print(BFS(BFS(1)[0])[1])